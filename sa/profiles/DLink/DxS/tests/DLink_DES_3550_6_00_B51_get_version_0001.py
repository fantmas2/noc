# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## DLink.DxS.get_version test
## Auto-generated by ./noc debug-script at 13.06.2012 23:06:27
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class DLink_DxS_get_version_Test(ScriptTestCase):
    script = "DLink.DxS.get_version"
    vendor = "DLink"
    platform = "DES-3550"
    version = "6.00.B51"
    input = {}
    result = {'attributes': {'Boot PROM': '5.00.011',
                'HW version': 'A5',
                'Serial Number': 'PL0K2A4000007'},
 'platform': 'DES-3550',
 'vendor': 'DLink',
 'version': '6.00.B51'}
    motd = ''
    cli = {
## 'show switch'
'show switch': """show switch
Command: show switch

Device Type       : DES-3550 Fast-Ethernet Switch
Combo Port Type   : 1000Base-LX + 1000Base-T
MAC Address       : 1C-AF-F7-02-E5-68
IP Address        : 192.168.99.69 (Manual)
VLAN Name         : default
Subnet Mask       : 255.255.255.0
Default Gateway   : 0.0.0.0
Boot PROM Version : Build 5.00.011
Firmware Version  : Build 6.00.B51
Hardware Version  : A5
Serial Number     : PL0K2A4000007
Power Status      : Main - Normal, Redundant - Not Present
System Name       : D-Link
System Location   : 
System Contact    : 
Spanning Tree     : Disabled
GVRP              : Disabled
IGMP Snooping     : Enabled
TELNET            : Enabled (TCP 23)
SSH               : Disabled
WEB               : Enabled (TCP 80)
RMON              : Disabled
Clipaging         : Disabled
Asymmetric VLAN   : Disabled
Password Encryption Status : Disabled
""", 
## 'disable clipaging'
'disable clipaging': """disable clipaging
Command: disable clipaging

Success.   
""", 
## 'enable clipaging'
'enable clipaging': """enable clipaging
Command: enable clipaging

Success.   
""", 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
