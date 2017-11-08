#!./bin/python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# build noc.models._MODELS manifest
# ----------------------------------------------------------------------
# Copyright (C) 2007-2015 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from collections import defaultdict

from django.db.models import Model
from django.db.models import get_models
# Third-party modules
from mongoengine.base.common import _document_registry
from mongoengine.document import Document
# NOC modules
from noc.lib.app.site import site
from noc.settings import INSTALLED_APPS


def build():
    def add(c):
        mp = c.__module__.split(".")
        if mp[0] != "noc":
            return
        module = mp[1]
        alias = "%s.%s" % (module, c.__name__)
        path = "%s.%s" % (c.__module__, c.__name__)
        models[module] += [(alias, path)]

    # Load all applications and models
    site.autodiscover()
    models = defaultdict(list)  # Module -> [(alias, path)]
    # Enumerate documents
    for c in _document_registry.itervalues():
        if issubclass(c, Document):
            add(c)
    # Enumerate models
    for c in get_models():
        if issubclass(c, Model):
            add(c)
    # Dump
    out = [
        "## model_id -> full class path",
        "## Generated by build-models.py",
        "_MODELS = {"
    ]
    for app in INSTALLED_APPS:
        if not app.startswith("noc."):
            continue
        module = app[4:]
        if not models[module]:
            continue
        out += ["    # %s models" % module]
        for alias, path in sorted(models[module], key=lambda x: x[0]):
            out += ["    \"%s\": \"%s\"," % (alias, path)]
    out[-1] = out[-1][:-1]  # Remove last comma
    out += ["}"]
    print "\n".join(out)


if __name__ == "__main__":
    build()
