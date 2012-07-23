//---------------------------------------------------------------------
// inv.interface L1 Store
//---------------------------------------------------------------------
// Copyright (C) 2007-2012 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.inv.interface.L1Store");

Ext.define("NOC.inv.interface.L1Store", {
    extend: "Ext.data.Store",
    model: null,
    fields: [
        {
            name: "id",
            type: "auto"
        },
        {
            name: "name",
            type: "string"
        },
        {
            name: "mac",
            type: "string"
        },
        {
            name: "description",
            type: "string"
        },
        {
            name: "ifindex",
            type: "int"
        },
        {
            name: "lag",
            type: "string"
        },
        {
            name: "link",
            type: "auto"
        },
        {
            name: "profile",
            type: "string"
        },
        {
            name: "profile__label",
            type: "string"
        },
        {
            name: "row_class",
            type: "string"
        }
    ],
    data: []
});
