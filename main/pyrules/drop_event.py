# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## drop envent
##----------------------------------------------------------------------
## INTERFACE: IEvent
##----------------------------------------------------------------------
## DESCRIPTION:
## Delete event
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
@pyrule
def drop_event(event):
    event.delete()
