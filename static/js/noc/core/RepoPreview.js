//---------------------------------------------------------------------
// NOC.core.RepoPreview
//---------------------------------------------------------------------
// Copyright (C) 2007-2012 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.core.RepoPreview");

Ext.define("NOC.core.RepoPreview", {
    extend: "NOC.core.ApplicationPanel",
    msg: "",
    layout: "fit",
    syntax: null,
    restUrl: null,
    historyHashPrefix: null,

    initComponent: function() {
        var me = this;

        me.revCombo = Ext.create("Ext.form.ComboBox", {
            fieldLabel: "Version",
            labelWidth: 45,
            width: 200,
            queryMode: "local",
            displayField: "ts_label",
            valueField: "id",
            store: Ext.create("Ext.data.Store", {
                fields: [
                    {
                        name: "id",
                        type: "auto"
                    },
                    {
                        name: "ts",
                        type: "date"
                    },
                    {
                        name: "ts_label",
                        mapping: "ts",
                        convert: function(v, record) {
                            return NOC.render.DateTime(record.get("ts"));
                        }
                    }
                ],
                data: []
            }),
            listeners: {
                scope: me,
                select: me.onSelectRev,
                specialkey: me.onRevSpecialKey
            }
        });

        me.diffCombo = Ext.create("Ext.form.ComboBox", {
            fieldLabel: "Compare",
            disabled: true,
            labelWidth: 45,
            width: 200,
            queryMode: "local",
            displayField: "ts_label",
            valueField: "id",
            store: Ext.create("Ext.data.Store", {
                fields: [
                    {
                        name: "id",
                        type: "auto"
                    },
                    {
                        name: "ts",
                        type: "date"
                    },
                    {
                        name: "ts_label",
                        mapping: "ts",
                        convert: function(v, record) {
                            return NOC.render.DateTime(record.get("ts"));
                        }
                    }
                ],
                data: []
            }),
            listeners: {
                scope: me,
                select: me.onSelectDiff,
                specialkey: me.onDiffSpecialKey
            }
        });

        me.reloadButton = Ext.create("Ext.button.Button", {
            glyph: NOC.glyph.refresh,
            text: "Reload",
            tooltip: "Reload",
            scope: me,
            handler: me.onReload
        });

        me.nextDiffButton = Ext.create("Ext.button.Button", {
            glyph: NOC.glyph.arrow_up,
            tooltip: "Next change",
            disabled: true,
            scope: me,
            handler: me.onNextDiff
        });

        me.prevDiffButton = Ext.create("Ext.button.Button", {
            glyph: NOC.glyph.arrow_down,
            tooltip: "Previous change",
            disabled: true,
            scope: me,
            handler: me.onPrevDiff
        });

        me.swapRevButton = Ext.create("Ext.button.Button", {
            glyph: NOC.glyph.exchange,
            tooltip: "Swap revisions",
            disabled: true,
            scope: me,
            handler: me.onSwapRev
        });

        me.lastDayButton = Ext.create("Ext.button.Button", {
            text: "Day",
            tooltip: "Last day's changes",
            toogleGroup: "diffrange",
            scope: me,
            handler: me.onLastPressed,
            diffRange: 1
        });

        me.lastWeekButton = Ext.create("Ext.button.Button", {
            text: "Week",
            tooltip: "Last week's changes",
            toogleGroup: "diffrange",
            scope: me,
            handler: me.onLastPressed,
            diffRange: 7
        });

        me.lastMonthButton = Ext.create("Ext.button.Button", {
            text: "Month",
            tooltip: "Last month's changes",
            toogleGroup: "diffrange",
            scope: me,
            handler: me.onLastPressed,
            diffRange: 30
        });

        Ext.apply(me, {
            dockedItems: [{
                xtype: "toolbar",
                dock: "top",
                items: [
                    {
                        itemId: "close",
                        text: "Close",
                        glyph: NOC.glyph.arrow_left,
                        scope: me,
                        handler: me.onClose
                    },
                    me.reloadButton,
                    "-",
                    me.revCombo,
                    me.swapRevButton,
                    me.diffCombo,
                    me.nextDiffButton,
                    me.prevDiffButton,
                    "-",
                    me.lastDayButton,
                    me.lastWeekButton,
                    me.lastMonthButton
                ]
            }],
            items: [{
                xtype: "container",
                autoScroll: true
            }]
        });
        me.callParent();
        //
        me.urlTemplate = Handlebars.compile(me.restUrl);
        me.titleTemplate = Handlebars.compile(me.previewName);
        me.viewer = null;
    },
    //
    afterRender: function() {
        var me = this;
        me.callParent();
        me.viewer = new CodeMirror(me.items.first().el.dom, {
            readOnly: true,
            lineNumbers: true
        });
    },
    //
    startPreview: function(record, backItem) {
        var me = this,
            bi = backItem === undefined? me.backItem : backItem;
        me.currentRecord = record;
        me.backItem = bi;
        // @todo: Replace to superclass call
        me.rootUrl = me.urlTemplate(record.data);
        me.setTitle(me.titleTemplate(record.data));
    },
    //
    preview: function(record, backItem) {
        var me = this;
        me.startPreview(record, backItem);
        me.requestText();
        me.requestRevisions();
    },
    //
    requestText: function() {
        var me = this,
            mask = me.setLoading({msg: "Loading"});
        Ext.Ajax.request({
            url: me.rootUrl,
            method: "GET",
            scope: me,
            success: function(response) {
                me.renderText(Ext.decode(response.responseText));
                mask.hide();
                if(me.historyHashPrefix) {
                    me.app.setHistoryHash(
                        me.currentRecord.get("id"),
                        me.historyHashPrefix
                    );
                }
            },
            failure: function() {
                mask.hide();
                NOC.error("Failed to get text");
            }
        });
    },
    //
    requestRevisions: function(callback) {
        var me = this;
        Ext.Ajax.request({
            url: me.rootUrl + "revisions/",
            method: "GET",
            scope: me,
            success: function(response) {
                var data = Ext.decode(response.responseText);
                me.revCombo.store.loadData(data);
                me.diffCombo.store.loadData(data);
                if(data.length > 0) {
                    me.revCombo.select([me.revCombo.store.getAt(0)]);
                }
                me.nextDiffButton.setDisabled(true);
                me.prevDiffButton.setDisabled(data.length === 0);
                Ext.callback(callback, me);
            },
            failure: function() {
                NOC.error("Failed to get revisions");
            }
        });
    },
    //
    requestRevision: function(rev) {
        var me = this,
            mask = me.setLoading({msg: "Loading"});
        Ext.Ajax.request({
            url: me.rootUrl + rev + "/",
            method: "GET",
            scope: me,
            success: function(response) {
                me.renderText(Ext.decode(response.responseText));
                mask.hide();
                if(me.historyHashPrefix) {
                    me.app.setHistoryHash(
                        me.currentRecord.get("id"),
                        me.historyHashPrefix,
                        rev
                    );
                }
            },
            failure: function() {
                NOC.error("Failed to get text");
                mask.hide();
            }
        });
    },
    //
    requestDiff: function(rev1, rev2) {
        var me = this,
            mask = me.setLoading({msg: "Loading"});
        Ext.Ajax.request({
            url: me.rootUrl + rev1 + "/" + rev2 + "/",
            method: "GET",
            scope: me,
            success: function(response) {
                me.renderText(Ext.decode(response.responseText), "diff");
                mask.hide();
                if(me.historyHashPrefix) {
                    me.app.setHistoryHash(
                        me.currentRecord.get("id"),
                        me.historyHashPrefix,
                        rev1,
                        rev2
                    );
                }
            },
            failure: function() {
                NOC.error("Failed to get diff");
                mask.hide();
            }
        });
    },
    //
    renderText: function(text, syntax) {
        var me = this;
        me.viewer.setValue(text);
    },
    //
    onSelectRev: function(combo, records, eOpts) {
        var me = this;
        me.requestRevision(records[0].get("id"));
        me.diffCombo.setDisabled(false);
        me.swapRevButton.setDisabled(false);
    },
    //
    requestCurrentDiff: function() {
        var me = this;
        me.requestDiff(
            me.diffCombo.getValue(),
            me.revCombo.getValue()
        );
    },
    //
    onSelectDiff: function(combo, records, eOpts) {
        var me = this;
        me.requestCurrentDiff();
    },
    //
    onRevSpecialKey: function(combo, evt, opts) {
        var me = this;
        if(evt.getKey() == evt.ESC) {
            combo.clearValue();
        }
    },
    //
    onDiffSpecialKey: function(combo, evt, opts) {
        var me = this;
        if(evt.getKey() == evt.ESC) {
            combo.clearValue();
            me.onSelectRev(me.revCombo, [me.revCombo.picker.getSelectionModel().lastSelected]);
        }
    },
    // Returns current selection index or null
    getRevIndex: function(combo) {
        var me = this,
            v = combo.getValue();
        return combo.store.findExact("id", v);
    },
    //
    setRevIndex: function(combo, index) {
        var me = this;
        combo.select([combo.store.getAt(index)]);
    },
    //
    onPrevDiff: function() {
        var me = this,
            rIndex = me.getRevIndex(me.revCombo),
            dIndex = me.getRevIndex(me.diffCombo);
        if(rIndex === dIndex - 1) {
            me.setRevIndex(me.revCombo, rIndex + 1);
            dIndex = rIndex + 2;
        } else {
            dIndex = rIndex + 1;
        }
        me.setRevIndex(me.diffCombo, dIndex);
        me.prevDiffButton.setDisabled(dIndex >= me.revCombo.store.data.length - 1);
        me.nextDiffButton.setDisabled(false);
        me.diffCombo.setDisabled(false);
        me.swapRevButton.setDisabled(false);
        me.requestCurrentDiff();
    },
    //
    onNextDiff: function() {
        var me = this,
            rIndex = me.getRevIndex(me.revCombo),
            dIndex = me.getRevIndex(me.diffCombo);
        if(rIndex === dIndex - 1) {
            rIndex -= 1;
            me.setRevIndex(me.revCombo, rIndex);
        }
        dIndex = rIndex + 1;
        me.setRevIndex(me.diffCombo, dIndex);
        me.prevDiffButton.setDisabled(false);
        me.nextDiffButton.setDisabled(rIndex <= 0);
        me.diffCombo.setDisabled(false);
        me.swapRevButton.setDisabled(false);
        me.requestCurrentDiff();
    },
    //
    onSwapRev: function() {
        var me = this,
            rIndex = me.getRevIndex(me.revCombo),
            dIndex = me.getRevIndex(me.diffCombo);
        me.setRevIndex(me.revCombo, dIndex);
        me.setRevIndex(me.diffCombo, rIndex);
        me.requestCurrentDiff();
    },
    //
    onLastPressed: function(button, evt) {
        var me = this,
            store = me.revCombo.store,
            rl = store.data.length - 1,
            i0 = me.getRevIndex(me.revCombo),
            t0 = i0 === 0 ? +(new Date()):+store.getAt(0).get("ts"),
            t1 = t0 - button.diffRange * 86400000,
            i1;
        if(i0 === 0 && +store.getAt(0).get("ts") <= t1) {
            NOC.info("Nothing changed");
            return;
        }
        for(i1 = i0 + 1; i1 < rl; i1 ++) {
            if(+store.getAt(i1).get("ts") <= t1)
                break;
        }
        me.setRevIndex(me.revCombo, i0);
        me.diffCombo.setDisabled(false);
        me.swapRevButton.setDisabled(false);
        me.setRevIndex(me.diffCombo, i1);
        me.requestCurrentDiff();
    },
    //
    onReload: function() {
        var me = this;
        me.requestText();
        me.requestRevisions();
    },
    //
    historyRevision: function(record, rev) {
        var me = this;
        me.startPreview(record);
        me.requestRevisions(function() {
            me.setRevIndex(
                me.revCombo,
                me.revCombo.store.findExact("id", rev)
            );
            me.diffCombo.setDisabled(false);
        });
        me.requestRevision(rev);
    },
    //
    historyDiff: function(record, rev1, rev2) {
        var me = this;
        me.startPreview(record);
        me.requestRevisions(function() {
            me.diffCombo.setDisabled(false);
            me.setRevIndex(
                me.revCombo,
                me.revCombo.store.findExact("id", rev2)
            );
            me.setRevIndex(
                me.diffCombo,
                me.diffCombo.store.findExact("id", rev1)
            );
        });
        me.requestDiff(rev1, rev2);
    }
});
