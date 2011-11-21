# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Cisco.IOS.get_switchport test
## Auto-generated by ./noc debug-script at 2011-11-21 14:37:53
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Cisco_IOS_get_switchport_Test(ScriptTestCase):
    script = "Cisco.IOS.get_switchport"
    vendor = "Cisco"
    platform = 's72033_rp'
    version = '12.2(18)SXF16'
    input = {}
    result = [{'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'Krivbass-Telekom',
  'interface': 'Gi 2/2',
  'members': [],
  'status': True,
  'tagged': [128,
             211,
             222,
             231,
             246,
             251,
             252,
             254,
             255,
             256,
             356,
             357,
             444,
             600],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'to_ludmila_catalyst',
  'interface': 'Gi 2/3',
  'members': [],
  'status': True,
  'tagged': [2, 3, 13, 127, 252, 254, 255, 256, 258, 333, 356, 444],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'pilot->sivolapa',
  'interface': 'Gi 2/4',
  'members': [],
  'status': True,
  'tagged': [114, 128, 215, 235, 246, 252, 254, 255, 256, 356],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'vpns-local-ifaces',
  'interface': 'Gi 2/5',
  'members': [],
  'status': True,
  'tagged': [4, 255],
  'untagged': 255},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'vpns-local-ifaces',
  'interface': 'Gi 2/6',
  'members': [],
  'status': True,
  'tagged': [4, 255],
  'untagged': 255},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'vpns-local-ifaces',
  'interface': 'Gi 2/7',
  'members': [],
  'status': True,
  'tagged': [4, 255],
  'untagged': 255},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'vpns-local-ifaces',
  'interface': 'Gi 2/8',
  'members': [],
  'status': True,
  'tagged': [4, 255],
  'untagged': 255},
 {'802.1Q Enabled': False,
  '802.1ad Tunnel': False,
  'description': 'iptv_trophy',
  'interface': 'Gi 2/9',
  'members': [],
  'status': True,
  'tagged': [],
  'untagged': 255},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'vpns-local-ifaces',
  'interface': 'Gi 2/10',
  'members': [],
  'status': False,
  'tagged': [4, 255],
  'untagged': 255},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'vpns-local-ifaces',
  'interface': 'Gi 2/11',
  'members': [],
  'status': True,
  'tagged': [4, 255],
  'untagged': 255},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'vpns-local-ifaces',
  'interface': 'Gi 2/14',
  'members': [],
  'status': True,
  'tagged': [4, 255],
  'untagged': 255},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'interface': 'Gi 2/15',
  'members': [],
  'status': True,
  'tagged': [2, 3, 255, 256],
  'untagged': 1},
 {'802.1Q Enabled': False,
  '802.1ad Tunnel': False,
  'interface': 'Gi 2/16',
  'members': [],
  'status': True,
  'tagged': [],
  'untagged': 3},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'vovan_maket',
  'interface': 'Gi 2/17',
  'members': [],
  'status': False,
  'tagged': [255],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'vovan_maket',
  'interface': 'Gi 2/18',
  'members': [],
  'status': False,
  'tagged': [255],
  'untagged': 255},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'vpns-local-ifaces',
  'interface': 'Gi 2/19',
  'members': [],
  'status': True,
  'tagged': [4, 255],
  'untagged': 255},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': '3845 Corporativ',
  'interface': 'Gi 2/20',
  'members': [],
  'status': True,
  'tagged': [3],
  'untagged': 1},
 {'802.1Q Enabled': False,
  '802.1ad Tunnel': False,
  'description': 'bras-local-10110',
  'interface': 'Gi 2/21',
  'members': [],
  'status': True,
  'tagged': [],
  'untagged': 255},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'bras-2-users',
  'interface': 'Gi 2/22',
  'members': [],
  'status': True,
  'tagged': [600,
             601,
             602,
             603,
             604,
             605,
             606,
             607,
             608,
             609,
             610,
             611,
             612,
             613,
             614,
             615,
             616,
             617,
             618,
             619,
             620,
             621,
             622,
             623,
             624,
             625,
             626,
             627,
             628,
             629,
             630,
             631,
             632,
             633,
             634,
             635,
             636,
             637,
             638,
             639,
             640,
             641,
             642,
             643,
             644,
             645,
             646,
             647,
             648,
             649,
             650,
             651,
             652,
             653,
             654,
             655,
             656,
             657,
             658,
             659,
             660,
             661,
             662,
             663,
             664,
             665,
             666,
             667,
             668,
             669,
             670,
             671,
             672,
             673,
             674,
             675,
             676,
             677,
             678,
             679,
             680,
             681,
             682,
             683,
             684,
             685,
             686,
             687,
             688,
             689,
             690,
             691,
             692,
             693,
             694,
             695,
             696,
             697,
             698,
             699],
  'untagged': 1},
 {'802.1Q Enabled': False,
  '802.1ad Tunnel': False,
  'interface': 'Gi 2/23',
  'members': [],
  'status': False,
  'tagged': [],
  'untagged': 3},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'NOC',
  'interface': 'Gi 2/24',
  'members': [],
  'status': True,
  'tagged': [3, 256],
  'untagged': 3},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'Vesta-L',
  'interface': 'Te 3/1',
  'members': [],
  'status': True,
  'tagged': [127, 252, 254, 255, 256, 356],
  'untagged': 1},
 {'802.1Q Enabled': False,
  '802.1ad Tunnel': False,
  'description': 'to 7600',
  'interface': 'Te 3/2',
  'members': [],
  'status': True,
  'tagged': [],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'dot1q trunk to SW(SEVER)',
  'interface': 'Te 3/3',
  'members': [],
  'status': True,
  'tagged': [9,
             12,
             13,
             123,
             128,
             217,
             237,
             249,
             251,
             252,
             254,
             255,
             256,
             356,
             357,
             444,
             600,
             601,
             602,
             603,
             604,
             605,
             606,
             607,
             608,
             609,
             610,
             611,
             612,
             613,
             614,
             615,
             616,
             617,
             618,
             619,
             620,
             621,
             622,
             623,
             624,
             625,
             626,
             627,
             628,
             629,
             630,
             631,
             632,
             633,
             634,
             635,
             636,
             637,
             638,
             639,
             640,
             641,
             642,
             643,
             644,
             645,
             646,
             647,
             648,
             649,
             650,
             651,
             652,
             653,
             654,
             655,
             656,
             657,
             658,
             659,
             660,
             661,
             662,
             663,
             664,
             665,
             666,
             667,
             668,
             669,
             670,
             671,
             672,
             673,
             674,
             675,
             676,
             677,
             678,
             679,
             680,
             681,
             682,
             683,
             684,
             685,
             686,
             687,
             688,
             689,
             690,
             691,
             692,
             693,
             694,
             695,
             696,
             697,
             698,
             699,
             700],
  'untagged': 1},
 {'802.1Q Enabled': True,
  '802.1ad Tunnel': False,
  'description': 'ludmila',
  'interface': 'Te 4/1',
  'members': [],
  'status': True,
  'tagged': [128, 254, 255, 256],
  'untagged': 1}]
    motd = '\n'
    cli = {
## 'show interfaces switchport'
'show interfaces switchport': """show interfaces switchport
Name: Gi2/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 12,13,128,254-256
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/2
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 128,211,222,231,246,251,252,254-256,356,357,444,600
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/3
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 2,3,13,127,252,254-256,258,333,356,444
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/4
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 114,128,215,235,246,252,254-256,356
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/5
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 4,255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/6
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 4,255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/7
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 4,255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/8
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 4,255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/9
Switchport: Enabled
Administrative Mode: static access
Operational Mode: static access
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: native
Negotiation of Trunking: Off
Access Mode VLAN: 255 (allubr->LAN)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: ALL
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/10
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: down
Administrative Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 4,255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/11
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 4,255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/14
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 4,255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/15
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 2,3,255,256
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/16
Switchport: Enabled
Administrative Mode: static access
Operational Mode: static access
Administrative Trunking Encapsulation: negotiate
Operational Trunking Encapsulation: native
Negotiation of Trunking: Off
Access Mode VLAN: 3 (network_10.111)
Trunking Native Mode VLAN: 3 (network_10.111)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 3
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/17
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: down
Administrative Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/18
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: down
Administrative Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/19
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 4,255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/20
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 3
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/21
Switchport: Enabled
Administrative Mode: static access
Operational Mode: static access
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: native
Negotiation of Trunking: Off
Access Mode VLAN: 255 (allubr->LAN)
Trunking Native Mode VLAN: 255 (allubr->LAN)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 255
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/22
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 600-699
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/23
Switchport: Enabled
Administrative Mode: static access
Operational Mode: down
Administrative Trunking Encapsulation: negotiate
Negotiation of Trunking: Off
Access Mode VLAN: 3 (network_10.111)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: ALL
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Gi2/24
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 3 (network_10.111)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 3,256
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Te3/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 127,252,254-256,356
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Te3/2
Switchport: Enabled
Administrative Mode: dynamic desirable
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: ALL
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Te3/3
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 9,12,13,123,128,217,237,249,251,252,254-256,356,357,
     444,600-700
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled


Name: Te4/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: 128,254-256
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Unknown unicast blocked: disabled
Unknown multicast blocked: disabled

""", 
## 'show interfaces description'
'show interfaces description': """show interfaces description
Interface                      Status         Protocol Description
Vl1                            admin down     down     
Vl3                            up             up       
Vl4                            up             up       
Vl254                          admin down     down     
Vl255                          up             up       10.110
Vl256                          up             up       
Gi2/1                          up             up       Satelit
Gi2/2                          up             up       Krivbass-Telekom
Gi2/3                          up             up       to_ludmila_catalyst
Gi2/4                          up             up       pilot->sivolapa
Gi2/5                          up             up       vpns-local-ifaces
Gi2/6                          up             up       vpns-local-ifaces
Gi2/7                          up             up       vpns-local-ifaces
Gi2/8                          up             up       vpns-local-ifaces
Gi2/9                          up             up       iptv_trophy
Gi2/10                         down           down     vpns-local-ifaces
Gi2/11                         up             up       vpns-local-ifaces
Gi2/12                         admin down     down     
Gi2/13                         admin down     down     
Gi2/14                         up             up       vpns-local-ifaces
Gi2/15                         up             up       
Gi2/16                         up             up       
Gi2/17                         down           down     vovan_maket
Gi2/18                         down           down     vovan_maket
Gi2/19                         up             up       vpns-local-ifaces
Gi2/20                         up             up       3845 Corporativ
Gi2/21                         up             up       bras-local-10110
Gi2/22                         up             up       bras-2-users
Gi2/23                         down           down     
Gi2/24                         up             up       NOC
Te3/1                          up             up       Vesta-L
Te3/2                          up             up       to 7600
Te3/3                          up             up       dot1q trunk to SW(SEVER)
Te3/4                          admin down     down     
Te4/1                          up             up       ludmila
Te4/2                          admin down     down     
Te4/3                          admin down     down     
Te4/4                          admin down     down     
Gi5/1                          admin down     down     
Gi5/2                          admin down     down     
Gi6/1                          admin down     down     
Gi6/2                          admin down     down     
Lo0                            up             up       """, 
'terminal length 0':  'terminal length 0\n', 
}
    snmp_get = {}
    snmp_getnext = {}
