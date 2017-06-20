# -*- coding: utf-8 -*-
"""
##----------------------------------------------------------------------
## fm.reportmetrics
##----------------------------------------------------------------------
## Copyright (C) 2007-2017 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""

## Python modules
import datetime
## Django modules
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
## NOC modules
from noc.sa.models.managedobjectprofile import ManagedObjectProfile
from noc.sa.models.managedobject import ManagedObject
from noc.inv.models.interface import Interface
from noc.inv.models.interfaceprofile import InterfaceProfile
from noc.core.influxdb.client import InfluxDBClient
from noc.lib.nosql import get_db
from noc.sa.models.useraccess import UserAccess
from noc.lib.app.simplereport import SimpleReport, TableColumn
from noc.core.translation import ugettext as _
from noc.sa.models.managedobjectselector import ManagedObjectSelector
from noc.sa.models.administrativedomain import AdministrativeDomain


class ReportForm(forms.Form):
    reporttype = forms.ChoiceField(choices=[
       ("load_interfaces",  _("Load Interfaces")),
       ("load_cpu",  _("Load CPU/Memory")),
       ("errors",  _("Errors on the Interface"))
    ], label=_("Report Type"))
    from_date = forms.CharField(
        widget=AdminDateWidget,
        label=_("From Date"),
        required=True
    )
    to_date = forms.CharField(
        widget=AdminDateWidget,
        label=_("To Date"),
        required=True
    )
    # skip_avail = forms.BooleanField(
    #     label=_("Skip full available"),
    #     required=False
    # )

    # managed_object = forms.ModelChoiceField(
    #    label=_("Managed Object"),
    #    required=False,
    #    queryset=ManagedObject.objects.filter()
    # )
    selectors = forms.ModelChoiceField(
        label=_("Selectors"),
        required=False,
        queryset=ManagedObjectSelector.objects.order_by("name")
    )
    administrative_domain = forms.ModelChoiceField(
        label=_("Administrative Domain"),
        required=False,
        queryset=AdministrativeDomain.objects.order_by("name")
    )
    object_profile = forms.ModelChoiceField(
        label=_("Object Profile"),
        required=False,
        queryset=ManagedObjectProfile.objects.exclude(name__startswith="tg.").order_by("name")
    )
    interface_profile = forms.ModelChoiceField(
        label=_("Interface Profile (For Load Interfaces Report Type)"),
        required=False,
        queryset=InterfaceProfile.objects.order_by("name")
    )
    zero = forms.BooleanField(
        label=_("Exclude 0"),
        required=False
    )
    percent = forms.BooleanField(
        label=_("Load interface in % (For Load Interfaces Report Type)"),
        required=False
    )
    filter_default = forms.BooleanField(
        label=_("Enable Default interface profile (For Load Interfaces Report Type)"),
        required=False
    )

class ReportTraffic(SimpleReport):
    title = _("Load Metrics")
    form = ReportForm

    def get_data(self, request, reporttype, from_date=None, to_date=None, object_profile=None, percent=None, filter_default=None, zero=None,
                 interface_profile=None, managed_object=None, selectors=None, administrative_domain=None, **kwargs):
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        f_d = datetime.datetime.strptime(from_date, "%d.%m.%Y")
        fd = f_d.strftime("%Y-%m-%dT%H:%M:%SZ")
        t_d = datetime.datetime.strptime(to_date, "%d.%m.%Y")
        td = t_d.strftime("%Y-%m-%dT23:59:59Z")
        if td.split("T")[0] == now.split("T")[0]:
            td = now
        # Interval days
        fd1 = td.split('T')
        td1 = fd.split('T')
        a = fd1[0].split('-')
        b = td1[0].split('-')
        aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
        bb = datetime.date(int(b[0]), int(b[1]), int(b[2]))
        cc = aa - bb
        dd = str(cc)
        interval = (dd.split()[0])
        # Load managed objects
        f = []
        in_p = []
        out_p = []
        columns = []
        if not request.user.is_superuser:
            mos = mos.filter(
                administrative_domain__in=UserAccess.get_domains(request.user))
        if selectors:
            mos = selectors.managed_objects
        if administrative_domain:
            mos = ManagedObject.objects.filter(is_managed=True, administrative_domain=administrative_domain)
        if object_profile:
            mos = ManagedObject.objects.filter(is_managed=True, object_profile=object_profile)
        if managed_object:
            mos = ManagedObject.objects.filter(is_managed=True, id=managed_object.id)
        if "load_interfaces" in reporttype:
            for res in InterfaceProfile.objects.filter():
                if res.name == "default" and not filter_default:
                    continue
                for o in mos:
                    ifaces = Interface.objects.filter(managed_object=o, type="physical", profile=res)
                    if interface_profile:
                        ifaces = Interface.objects.filter(managed_object=o, type="physical", profile=interface_profile)
                    for j in ifaces:
                        # print o.name, "," , o.platform  , ",", o.address, ",", j.name, ",", j.in_speed, ",", j.out_speed,",",j.description
                        # quit()
                        client = InfluxDBClient()
                        query1 = [
                            "SELECT percentile(\"value\", 98) FROM \"Interface | Load | In\" WHERE \"object\" = '%s' AND \"interface\" = '%s' AND time >= '%s' AND time <= '%s';" % (
                                o.name, j.name, fd, td)]
                        result1 = client.query(query1)
                        r = list(result1)
                        if len(r) > 0:
                            r = r[0]
                            r1 = r["percentile"]
                        else:
                            r1 = 0
                        query2 = [
                            "SELECT percentile(\"value\", 98) FROM \"Interface | Load | Out\" WHERE \"object\" = '%s' AND \"interface\" = '%s' AND time >= '%s' AND time <= '%s';" % (
                                o.name, j.name, fd, td)]
                        result2 = client.query(query2)
                        r = list(result2)
                        if len(r) > 0:
                            r = r[0]
                            r2 = r["percentile"]
                        else:
                            r2 = 0

                        if j.in_speed and r1 > 0:
                            in_p = (r1 / 1000.0) / (j.in_speed / 100.0)
                            in_p = round(in_p, 2)
                        if j.out_speed and r2 > 0:
                            out_p = (r2 / 1000.0) / (j.out_speed / 100.0)
                            out_p = round(out_p, 2)
                        if percent and zero:
                            columns = [_("Managed Object"), _("Address"), _("Int Name"), _("Int Descr"),
                                       TableColumn(_("IN bps"), align="right"),
                                       TableColumn(_("IN %"), align="right"),
                                       TableColumn(_("OUT bps"), align="right"),
                                       TableColumn(_("OUT %"), align="right"),
                                       TableColumn(_("Interval days"), align="right")
                                       ]
                            if r1 != 0 and r2 != 0:
                                f += [(
                                    o.name,
                                    o.address,
                                    j.name,
                                    j.description,
                                    int(r1),
                                    in_p,
                                    int(r2),
                                    out_p,
                                    interval
                                )]
                        elif zero:
                            columns = [_("Managed Object"), _("Address"), _("Int Name"), _("Int Descr"),
                                       TableColumn(_("IN bps"), align="right"),
                                       TableColumn(_("OUT bps"), align="right"),
                                       TableColumn(_("Interval days"), align="right")
                                       ]
                            if r1 != 0 and r2 != 0:
                                f += [(
                                    o.name,
                                    o.address,
                                    j.name,
                                    j.description,
                                    int(r1),
                                    int(r2),
                                    interval
                                )]
                        elif percent:
                            columns = [_("Managed Object"), _("Address"), _("Int Name"), _("Int Descr"),
                                       TableColumn(_("IN bps"), align="right"),
                                       TableColumn(_("IN %"), align="right"),
                                       TableColumn(_("OUT bps"), align="right"),
                                       TableColumn(_("OUT %"), align="right"),
                                       TableColumn(_("Interval days"), align="right")
                                       ]
                            f += [(
                                o.name,
                                o.address,
                                j.name,
                                j.description,
                                int(r1),
                                in_p,
                                int(r2),
                                out_p,
                                interval
                            )]

                        else:
                            columns = [_("Managed Object"), _("Address"), _("Int Name"), _("Int Descr"),
                                       TableColumn(_("IN bps"), align="right"),
                                       TableColumn(_("OUT bps"), align="right"),
                                       TableColumn(_("Interval days"), align="right")
                                       ]
                            f += [(
                                o.name,
                                o.address,
                                j.name,
                                j.description,
                                int(r1),
                                int(r2),
                                interval
                            )]

        if "errors" in reporttype:
            for res in InterfaceProfile.objects.filter():
                if res.name == "default" and not filter_default:
                    continue
                for o in mos:
                    ifaces = Interface.objects.filter(managed_object=o, type="physical", profile=res)
                    if interface_profile:
                        ifaces = Interface.objects.filter(managed_object=o, type="physical", profile=interface_profile)
                    for j in ifaces:
                        # print o.name, "," , o.platform  , ",", o.address, ",", j.name, ",", j.in_speed, ",", j.out_speed,",",j.description
                        # quit()
                        client = InfluxDBClient()
                        query1 = [
                            "SELECT percentile(\"value\", 98) FROM \"Interface | Errors | In\" WHERE \"object\" = '%s' AND \"interface\" = '%s' AND time >= '%s' AND time <= '%s';" % (
                                o.name, j.name, fd, td)]
                        result1 = client.query(query1)
                        r = list(result1)
                        if len(r) > 0:
                            r = r[0]
                            r1 = r["percentile"]
                        else:
                            r1 = 0
                        query2 = [
                            "SELECT percentile(\"value\", 98) FROM \"Interface | Errors | Out\" WHERE \"object\" = '%s' AND \"interface\" = '%s' AND time >= '%s' AND time <= '%s';" % (
                                o.name, j.name, fd, td)]
                        result2 = client.query(query2)
                        r = list(result2)
                        if len(r) > 0:
                            r = r[0]
                            r2 = r["percentile"]
                        else:
                            r2 = 0

                        query11 = [
                            "SELECT percentile(\"value\", 98) FROM \"Interface | Discards | In\" WHERE \"object\" = '%s' AND \"interface\" = '%s' AND time >= '%s' AND time <= '%s';" % (
                                o.name, j.name, fd, td)]
                        result11 = client.query(query11)
                        r = list(result11)
                        if len(r) > 0:
                            r = r[0]
                            r11 = r["percentile"]
                        else:
                            r11 = 0

                        query22 = [
                            "SELECT percentile(\"value\", 98) FROM \"Interface | Discards | Out\" WHERE \"object\" = '%s' AND \"interface\" = '%s' AND time >= '%s' AND time <= '%s';" % (
                                o.name, j.name, fd, td)]
                        result22 = client.query(query22)
                        r = list(result22)
                        if len(r) > 0:
                            r = r[0]
                            r22 = r["percentile"]
                        else:
                            r22 = 0

                        if zero:
                            columns = [_("Managed Object"), _("Address"), _("Int Name"), _("Int Descr"),
                                       TableColumn(_("Errors IN"), align="right"),
                                       TableColumn(_("Errors OUT"), align="right"),
                                       TableColumn(_("Discards IN"), align="right"),
                                       TableColumn(_("Discards OUT"), align="right"),
                                       TableColumn(_("Interval days"), align="right")
                                       ]
                            if r1 != 0 and r2 != 0:
                                f += [(
                                    o.name,
                                    o.address,
                                    j.name,
                                    j.description,
                                    int(r1),
                                    int(r2),
                                    int(r11),
                                    int(r22),
                                    interval
                                )]
                        else:
                            columns = [_("Managed Object"), _("Address"), _("Int Name"), _("Int Descr"),
                                       TableColumn(_("Errors IN"), align="right"),
                                       TableColumn(_("Errors OUT"), align="right"),
                                       TableColumn(_("Discards IN"), align="right"),
                                       TableColumn(_("Discards OUT"), align="right"),
                                       TableColumn(_("Interval days"), align="right")
                                       ]
                            f += [(
                                o.name,
                                o.address,
                                j.name,
                                j.description,
                                int(r1),
                                int(r2),
                                int(r11),
                                int(r22),
                                interval
                            )]

        if "load_cpu" in reporttype:
                for o in mos:
                    # print o.name, "," , o.platform  , ",", o.address, ",", j.name, ",", j.in_speed, ",", j.out_speed,",",j.description
                    # quit()
                    client = InfluxDBClient()
                    query1 = [
                        "SELECT percentile(\"value\", 98) FROM \"CPU | Usage\" WHERE \"object\" = '%s' AND time >= '%s' AND time <= '%s';" % (
                            o.name, fd, td)]
                    result1 = client.query(query1)
                    r = list(result1)
                    if len(r) > 0:
                        r = r[0]
                        r1 = r["percentile"]
                    else:
                        r1 = 0
                    query2 = [
                        "SELECT percentile(\"value\", 98) FROM \"Memory | Usage\" WHERE \"object\" = '%s' AND time >= '%s' AND time <= '%s';" % (
                            o.name, fd, td)]
                    result2 = client.query(query2)
                    r = list(result2)
                    if len(r) > 0:
                        r = r[0]
                        r2 = r["percentile"]
                    else:
                        r2 = 0
                    if zero:
                        columns = [_("Managed Object"), _("Address"),
                                   TableColumn(_("CPU | Usage %"), align="right"),
                                   TableColumn(_("Memory | Usage %"), align="right"),
                                   TableColumn(_("Interval days"), align="right")
                                   ]
                        if r1 != 0 and r2 != 0:
                            f += [(
                                o.name,
                                o.address,
                                int(r1),
                                int(r2),
                                interval
                            )]
                    else:
                        columns = [_("Managed Object"), _("Address"),
                                   TableColumn(_("CPU | Usage %"), align="right"),
                                   TableColumn(_("Memory | Usage %"), align="right"),
                                   TableColumn(_("Interval days"), align="right")
                                   ]
                        f += [(
                            o.name,
                            o.address,
                            int(r1),
                            int(r2),
                            interval
                        )]
        return self.from_dataset(
            title=self.title,
            columns=columns,
            data=f,
            enumerate=True
        )