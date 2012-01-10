# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## gis.map application
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.app import ExtApplication, view
from noc.gis.models import Map
from noc.settings import config


class MapAppplication(ExtApplication):
    """
    gis.map application
    """
    title = "Map"
    menu = "Map"

    @view("^layers/$", access="view", api=True)
    def api_layers(self, request):
        """
        Return list of active layers
        :param request:
        :return:
        """
        enable_xyz = config.get("gis", "enable_xyz_maps")
        enable_tms = config.get("gis", "enable_tms_maps")
        layers = []
        for m in Map.objects.filter(is_active=True).order_by("name"):
            # XYZ layer
            if enable_xyz:
                layers += [{
                    "name": "%s (XYZ)" % m.name,
                    "type": "XYZ",
                    "url": "/gis/tms/%s/${z}/${x}/${y}.png" % m.id
                }]
            # TMS layer
            if enable_tms:
                layers += [{
                    "name": "%s (TMS)" % m.name,
                    "type": "TMS",
                    "layername": "%s" % m.id
                }]
        return layers

    @view(url="^$", access="view")
    def view_index(self, request):
        t_maps = [(m.id, m.name)
                  for m in Map.objects.filter(is_active=True).order_by("name")]
        return self.render(request, "index.html", t_maps=t_maps)

