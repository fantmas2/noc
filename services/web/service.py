#!./bin/python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Web service
# ---------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Third-party modules
import tornado.web
import tornado.httpserver
import tornado.gen
import tornado.wsgi
import django.core.handlers.wsgi
# NOC modules
from noc.config import config
from noc.core.service.base import Service
from noc.main.models.customfield import CustomField
from noc.core.perf import metrics


class WebService(Service):
    name = "web"
    api = []
    use_translation = True
    if config.features.traefik:
        traefik_backend = "web"
        traefik_frontend_rule = "PathPrefix:/"

    def __init__(self):
        super(WebService, self).__init__()

    def get_handlers(self):
        return [
            # Pass to NOC
            (r"^.*$", NOCWSGIHandler, {"service": self})
        ]

    def on_activate(self):
        # Initialize audit trail
        from noc.main.models.audittrail import AuditTrail
        AuditTrail.install()
        # Initialize site
        self.logger.info("Registering web applications")
        from noc.lib.app.site import site
        site.service = self
        site.autodiscover()
        # Install Custom fields
        CustomField.install_fields()

    def get_backend_weight(self):
        return config.web.max_threads

    def get_backend_limit(self):
        return config.web.max_threads


class NOCWSGIHandler(tornado.web.RequestHandler):
    def initialize(self, service):
        self.service = service
        self.wsgi = NOCWSGIContainer(
            self.service,
            django.core.handlers.wsgi.WSGIHandler()
        )
        self.executor = self.service.get_executor("max")
        self.backend_id = "%s (%s:%s)" % (
            self.service.service_id,
            self.service.address, self.service.port)

    @tornado.gen.coroutine
    def prepare(self):
        self.set_header("X-NOC-Backend", self.backend_id)
        yield self.executor.submit(self.wsgi, self.request)
        self._finished = True


class NOCWSGIContainer(tornado.wsgi.WSGIContainer):
    def __init__(self, service, wsgi):
        super(NOCWSGIContainer, self).__init__(wsgi)
        self.service = service

    def _log(self, status_code, request):
        method = request.method
        uri = request.uri
        remote_ip = request.remote_ip
        user = request.headers.get("Remote-User", "-")
        agent = request.headers.get("User-Agent", "-")
        referer = request.headers.get("Referer", "-")
        self.service.logger.info(
            "%s %s - \"%s %s\" HTTP/1.1 %s \"%s\" %s %.2fms",
            remote_ip, user, method, uri, status_code,
            referer, agent,
            1000.0 * request.request_time()
        )
        metrics["http_requests"] += 1
        metrics["http_requests_%s" % method.lower()] += 1
        metrics["http_response_%s" % status_code] += 1


if __name__ == "__main__":
    WebService().start()
