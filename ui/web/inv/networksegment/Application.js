//---------------------------------------------------------------------
// inv.networksegment application
//---------------------------------------------------------------------
// Copyright (C) 2007-2015 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.inv.networksegment.Application");

Ext.define("NOC.inv.networksegment.Application", {
    extend: "NOC.core.ModelApplication",
    requires: [
        "NOC.inv.networksegment.Model",
        "NOC.inv.networksegment.LookupField",
        "NOC.sa.managedobjectselector.LookupField",
        "Ext.ux.form.DictField"
    ],
    model: "NOC.inv.networksegment.Model",
    search: true,
    treeFilter: "parent",

    initComponent: function() {
        var me = this;

        me.ITEM_EFFECTIVE_SETTINGS = me.registerItem(
            "NOC.inv.networksegment.EffectiveSettingsPanel"
        );

        me.settingsButton = Ext.create("Ext.button.Button", {
            text: __("Effective Settings"),
            glyph: NOC.glyph.file,
            scope: me,
            handler: me.onEffectiveSettings
        });

        me.showMapButton = Ext.create("Ext.button.Button", {
            text: __("Show Map"),
            glyph: NOC.glyph.globe,
            scope: me,
            handler: me.onShowMap
        });

        Ext.apply(me, {
            columns: [
                {
                    text: __("Parent"),
                    dataIndex: "parent",
                    width: 200,
                    renderer: NOC.render.Lookup("parent")
                },
                {
                    text: __("Name"),
                    dataIndex: "name",
                    width: 200
                },
                {
                    text: __("Description"),
                    dataIndex: "description",
                    flex: 1
                },
                {
                    text: __("Tags"),
                    dataIndex: "tags",
                    width: 100,
                    renderer: NOC.render.Tags
                },
                {
                    text: __("Selector"),
                    dataIndex: "selector",
                    width: 100,
                    renderer: NOC.render.Lookup("selector")
                },
                {
                    text: __("Obj."),
                    dataIndex: "count",
                    width: 30,
                    align: "right",
                    sortable: false,
                    renderer: NOC.render.Badge
                }
            ],

            fields: [
                {
                    name: "name",
                    xtype: "textfield",
                    fieldLabel: __("Name"),
                    uiStyle: "large",
                    allowBlank: false
                },
                {
                    name: "parent",
                    xtype: "inv.networksegment.LookupField",
                    fieldLabel: __("Parent"),
                    uiStyle: "large",
                    allowBlank: true
                },
                {
                    name: "description",
                    xtype: "textarea",
                    fieldLabel: __("Description"),
                    uiStyle: "extra",
                    allowBlank: true
                },
                {
                    name: "sibling",
                    xtype: "inv.networksegment.LookupField",
                    fieldLabel: __("Sibling"),
                    uiStyle: "large",
                    allowBlank: true
                },
                {
                    name: "settings",
                    xtype: "dictfield",
                    fieldLabel: __("Settings")
                },
                {
                    name: "selector",
                    xtype: "sa.managedobjectselector.LookupField",
                    fieldLabel: __("Selector"),
                    allowBlank: true
                },
                {
                    name: "tags",
                    xtype: "tagsfield",
                    fieldLabel: __("Tags"),
                    allowBlank: true
                }
            ],

            formToolbar: [
                me.settingsButton,
                me.showMapButton
            ]
        });
        me.callParent();
    },
    //
    onEffectiveSettings: function() {
        var me = this;
        me.previewItem(me.ITEM_EFFECTIVE_SETTINGS, me.currentRecord);
    },
    //
    onShowMap: function() {
        var me = this;
        NOC.launch("inv.map", "history", {
            args: [me.currentRecord.get("id")]
        });
    }
});