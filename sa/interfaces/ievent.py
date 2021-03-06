# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# IEvent interface
# ---------------------------------------------------------------------
# Copyright (C) 2007-2010 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------
"""
"""
from noc.core.interface.base import BaseInterface
from base import InstanceOfParameter


class IEvent(BaseInterface):
    event = InstanceOfParameter("Event")
