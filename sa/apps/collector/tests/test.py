# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## sa.collector unittes
##----------------------------------------------------------------------
## Copyright (C) 2007-2014 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import RestModelTestCase, unittest


@unittest.skip("Not ready")
class CollectorTestCase(RestModelTestCase):
    app = "sa.collector"

    scenario = [
        {
            "GET": {
                # key: value
            },
            "POST": {
                # key: value
            },
            "PUT": {
                # key: value
            }
        }
    ]