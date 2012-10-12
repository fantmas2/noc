# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Cisco.IOS.get_version test
## Auto-generated by ./noc debug-script at 12.10.2012 17:56:14
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Cisco_IOS_get_version_Test(ScriptTestCase):
    script = "Cisco.IOS.get_version"
    vendor = "Cisco"
    platform = "C2951"
    version = "15.0(1)M5"
    input = {}
    result = {'attributes': {'image': 'C2951-UNIVERSALK9-M'},
 'platform': 'C2951',
 'vendor': 'Cisco',
 'version': '15.0(1)M5'}
    motd = 'Authentication successfull your privilege level is 15\n\n'
    cli = {
'terminal length 0':  'terminal length 0\n', 
}
    snmp_get = {'1.3.6.1.2.1.1.1.0': 'Cisco IOS Software, C2951 Software (C2951-UNIVERSALK9-M), Version 15.0(1)M5, RELEASE SOFTWARE (fc2)\r\nTechnical Support: http://www.cisco.com/techsupport\r\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\r\nCompiled Wed 23-Feb-11 16:04 by prod_rel_team'}
    snmp_getnext = {}
    http_get = {}
