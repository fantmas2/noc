# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Application classes
# ---------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC modules
from .site import *
from .access import *
from .application import *
from .modelapplication import *
from .extapplication import *
from .extmodelapplication import *
from .extdocapplication import *
from noc.config import config


def setup_processor(request):
    """
    Setup Context Processor.
    Used via TEMPLATE_CONTEXT_PROCESSORS variable in settings.py
    Adds "setup" variable to context.
    "setup" is a hash of
        "installation_name"

    :param request:
    :return:
    """
    favicon_url = config.customization.favicon_url
    if favicon_url.endswith(".png"):
        favicon_mime = "image/png"
    elif favicon_url.endswith(".jpg") or favicon_url.endswith(".jpeg"):
        favicon_mime = "image/jpeg"
    else:
        favicon_mime = None

    return {
        "setup": {
            "installation_name": config.installation_name,
            "logo_url": config.customization.logo_url,
            "logo_width": config.customization.logo_width,
            "logo_height": config.customization.logo_height,
            "favicon_url": favicon_url,
            "favicon_mime": favicon_mime,
        }
    }
