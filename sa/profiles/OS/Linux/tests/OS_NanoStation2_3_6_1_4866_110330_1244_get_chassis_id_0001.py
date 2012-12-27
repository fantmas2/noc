# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## OS.Linux.get_chassis_id test
## Auto-generated by ./noc debug-script at 27.12.2012 09:57:45
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class OS_Linux_get_chassis_id_Test(ScriptTestCase):
    script = "OS.Linux.get_chassis_id"
    vendor = "OS"
    platform = "NanoStation2"
    version = "3.6.1.4866.110330.1244"
    input = {}
    result = {'first_chassis_mac': '00:15:6D:DE:A3:3B',
 'last_chassis_mac': '00:15:6D:DE:A3:3B'}
    motd = "\n\nBusyBox v1.01 (2011.03.30-09:47+0000) Built-in shell (ash)\nEnter 'help' for a list of built-in commands.\n\n"
    cli = {
'export LANG=en_GB.UTF-8':  'export LANG=en_GB.UTF-8\n', 
## 'brctl show'
'brctl show': """brctl show
bridge name\tbridge id\t\tSTP enabled\tinterfaces
br146\t\t8000.00156ddea33b\tno\t\tath0.146
\t\t\t\t\t\t\teth0.146
br140\t\t8000.00156ddea33b\tno\t\tath0.140
\t\t\t\t\t\t\teth0.140
br100\t\t8000.00156ddea33b\tno\t\tath0.100
\t\t\t\t\t\t\teth0.100
br98\t\t8000.00156ddea33b\tno\t\teth0.98
\t\t\t\t\t\t\tath0.98""", 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
