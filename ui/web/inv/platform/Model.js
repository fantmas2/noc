//---------------------------------------------------------------------
// inv.platform Model
//---------------------------------------------------------------------
// Copyright (C) 2007-2017 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.inv.platform.Model");

Ext.define("NOC.inv.platform.Model", {
    extend: "Ext.data.Model",
    rest_url: "/inv/platform/",

    fields: [
        {
            name: "id",
            type: "string"
        },
        {
            name: "vendor",
            type: "string"
        },
        {
            name: "vendor__label",
            type: "string",
            persist: false
        },
        {
            name: "name",
            type: "string"
        },
        {
            name: "uuid",
            type: "string"
        },
        {
            name: "is_builtin",
            type: "boolean",
            persist: false
        },
        {
            name: "full_name",
            type: "string",
            persist: false
        }
    ]
});