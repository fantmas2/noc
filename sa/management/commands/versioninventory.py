# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Run version inventory
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import sys
## Django modules
from django.core.management.base import BaseCommand, CommandError
from noc.sa.models import ManagedObjectSelector, ManagedObject, ReduceTask


## Reduce task script
def reduce_script(task):
    import csv
    import sys

    d_headers = ["vendor", "platform", "version"]
    a_headers = set()
    # Collect result
    r = []
    for mt in task.maptask_set.all():
        if mt.status == "C":
            r += [(mt.managed_object, mt.script_result)]
            for h in mt.script_result:
                if h not in d_headers:
                    a_headers.add(h)
        else:
            r += [(mt.managed_object, {})]
    # Format result
    data = []
    headers = d_headers + sorted(a_headers)
    for o, v in r:
        row = [o.name, o.address]
        for h in headers:
            if h in v:
                row += [str(v)]
            else:
                row += [""]
    data = sorted(data, key=lambda x: x[0])
    writer = csv.writer(sys.stdout)
    writer.writerow(headers)
    writer.writerows(data)


class Command(BaseCommand):
    help = "Run version inventory"

    def _usage(self):
        print "./noc versioninventory <obj1> [ ... <objN> ]"
        print "Where <obj> is either:"
        print "   * managed object's name"
        print "   * @<selector name> for use from selector"
        sys.exit(1)

    def handle(self, *args, **options):
        if not args:
            self._usage()
        # Find objects
        objects = set()
        for o in args:
            if o.startswith("@"):
                # Selector
                try:
                    s = ManagedObjectSelector.objects.get(name=o[1:])
                except ManagedObjectSelector.DoesNotExist:
                    raise CommandError("Selector '%s' not found" % o[1:])
                objects.update([mo.name for mo in s.managed_objects])
            else:
                try:
                    s = ManagedObject.objects.get(name=o)
                except ManagedObject.DoesNotExist:
                    raise CommandError("Object '%s' not found" % o)
                objects.add(s.name)
        # Run MRT
        t = ReduceTask.create_task(list(objects), reduce_script, {},
                                   "get_version", {}, 0)
        t.get_result()
