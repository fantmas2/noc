//---------------------------------------------------------------------
// main.language application
//---------------------------------------------------------------------
// Copyright (C) 2007-2011 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.main.language.Application");

Ext.define("NOC.main.language.Application", {
    extend: "NOC.core.ModelApplication",
    uses: ["NOC.main.language.Model"],
    
    model: "NOC.main.language.Model",
    
    columns: [
        {
            text: "Name",
            dataIndex: "name"
        },
        {
            text: "Native Name",
            dataIndex: "native_name"
        },
        {
            text: "Active",
            dataIndex: "is_active"
        }
    ],
    
    fields: [
        {
            xtype: "textfield",
            fieldLabel: "Name",
            name: "name",
            allowBlank: false
        },

        {
            xtype: "textfield",
            fieldLabel: "Native Name",
            name: "native_name",
            allowBlank: false
        },
        
        {
            xtype: "checkboxfield",
            boxLabel: "Is Active",
            name: "is_active",
            inputValue: true
        }
    ]
});
