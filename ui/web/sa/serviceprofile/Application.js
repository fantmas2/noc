//---------------------------------------------------------------------
// sa.serviceprofile application
//---------------------------------------------------------------------
// Copyright (C) 2007-2016 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.sa.serviceprofile.Application");

Ext.define("NOC.sa.serviceprofile.Application", {
    extend: "NOC.core.ModelApplication",
    requires: [
        "NOC.sa.serviceprofile.Model",
        "NOC.main.ref.glyph.LookupField",
        "NOC.inv.interfaceprofile.LookupField"
    ],
    model: "NOC.sa.serviceprofile.Model",
    search: true,

    initComponent: function() {
        var me = this;

        Ext.apply(me, {
            columns: [
                {
                    text: __("Icon"),
                    data_index: "glyph",
                    width: 25,
                    renderer: function(v) {
                        if(v !== undefined && v !== "")
                        {
                            return "<i class='" + v + "'></i>";
                        } else {
                            return "";
                        }
                    }
                },
                {
                    text: __("Name"),
                    dataIndex: "name",
                    width: 200
                },
                {
                    text: __("Code"),
                    dataIndex: "code",
                    width: 100
                },
                {
                    text: __("Summary"),
                    dataIndex: "show_in_summary",
                    width: 50,
                    renderer: NOC.render.Bool
                },
                {
                    text: __("Description"),
                    dataIndex: "description",
                    flex: 1
                }
            ],
            fields: [
                {
                    name: "name",
                    xtype: "textfield",
                    fieldLabel: __("Name"),
                    allowBlank: false,
                    uiStyle: "medium"
                },
                {
                    name: "description",
                    xtype: "textarea",
                    fieldLabel: __("Description"),
                    allowBlank: true,
                    uiStyle: "extra"
                },
                {
                    name: "code",
                    xtype: "textfield",
                    fieldLabel: __("Code"),
                    allowBlank: true,
                    uiStyle: "medium"
                },
                {
                    name: "card_title_template",
                    xtype: "textfield",
                    fieldLabel: __("Title Template"),
                    uiStyle: "extra",
                    allowBlank: true
                },
                {
                    name: "glyph",
                    xtype: "main.ref.glyph.LookupField",
                    fieldLabel: __("Icon"),
                    allowBlank: true,
                    uiStyle: "large"
                },
                {
                    name: "show_in_summary",
                    xtype: "checkbox",
                    boxLabel: __("Show in summary"),
                    allowBlank: true
                },
                {
                    name: "interface_profile",
                    xtype: "inv.interfaceprofile.LookupField",
                    fieldLabel: __("Interface Profile"),
                    allowBlank: true
                },
                {
                    name: "weight",
                    xtype: "numberfield",
                    fieldLabel: __("Alarm weight"),
                    allowBlank: true,
                    uiStyle: "small"
                }
            ]
        });
        me.callParent();
    }
});