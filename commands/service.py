# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Service command
##----------------------------------------------------------------------
## Copyright (C) 2007-2015 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Third-party modules
import consul
## NOC modules
from noc.core.management.base import BaseCommand


class Command(BaseCommand):
    system_services = ["mongod", "postgres", "consul"]

    def handle(self, *args, **options):
        self.out("Creating Consul Client", 1)
        c = consul.Consul()
        self.out("Requesting services", 1)
        s_mask = "%-20s %-12s %-40s %s"
        print s_mask % ("Service", "Node", "URL", "Tags")
        index, service = c.catalog.services()
        for sn in service:
            index, instances = c.catalog.service(sn)
            for si in instances:
                if si["ServiceName"] in self.system_services:
                    url = "%s:%s" % (si["Address"], si["ServicePort"])
                else:
                    url = "http://%s:%s/api/%s/" % (
                        si["Address"], si["ServicePort"],
                        si["ServiceName"]
                    )
                print s_mask % (
                    si["ServiceName"],
                    si["Node"],
                    url,
                    ",".join(si.get("ServiceTags", []) or [])
                )

if __name__ == "__main__":
    Command().run()