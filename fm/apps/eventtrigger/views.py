# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## EventTrigger Manager
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Django modules
from django.contrib import admin
## NOC modules
from noc.lib.app import ModelApplication
from noc.fm.models import EventTrigger


class EventTriggerAdmin(admin.ModelAdmin):
    list_display = ["name", "is_enabled", "event_class_re", "condition",
            "time_pattern", "selector", "notification_group",
            "template", "pyrule"]
    list_filter = ["is_enabled"]


class EventTriggerApplication(ModelApplication):
    model = EventTrigger
    model_admin = EventTriggerAdmin
    menu = "Setup | Event Triggers"
