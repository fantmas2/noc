# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## IGetMPLSVPN interface
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from base import *


class IGetMPLSVPN(Interface):
    returns = ListOfParameter(element=DictParameter(attrs={
        # VPN type
        "type": StringParameter(choices=["VRF", "VPLS", "VLL"]),
        # VPN state. True - active, False - inactive
        "status": BooleanParameter(default=True),
        # Unique VPN name
        "name": StringParameter(),
        # Optional description
        "description": StringParameter(required=False),
        # RD, may be omitted for VRF-lite
        "rd": RDParameter(required=False),
        # List of interfaces
        "interfaces": ListOfParameter(element=InterfaceNameParameter())
    }))
    template = "interfaces/igetmplsvpn.html"
