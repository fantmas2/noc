# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Usage: debug-script <profile> <script> <stream-url>
##
## WARNING!!!
## This module implements part of activator functionality.
## Sometimes via dirty hacks
##----------------------------------------------------------------------
## Copyright (C) 2007-2009 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
from __future__ import with_statement
from django.core.management.base import BaseCommand
from noc.sa.profiles import profile_registry
from noc.sa.script import script_registry,scheme_id
from noc.sa.activator import Service,ServersHub
from noc.sa.protocols.sae_pb2 import *
from noc.sa.rpc import TransactionFactory
import logging,sys,ConfigParser,Queue,time,cPickle,threading,signal,os,datetime,pprint
from noc.lib.url import URL
from noc.lib.nbsocket import SocketFactory
from optparse import OptionParser, make_option
from noc.lib.validators import is_int

class Controller(object): pass
##
##
##
class SessionCan(object):
    def __init__(self,script_name,input={}):
        self.cli={} # Command -> result
        self.input=input
        self.result=None
        self.motd=""
        self.script_name=script_name
        self.snmp_get={}
        self.snmp_getnext={}
    ## Store data
    def save_interaction(self,provider,cmd,data):
        if provider=="cli":
            self.cli[cmd]=data
    ##
    def save_snmp_get(self,oid,result):
        self.snmp_get[oid]=result
    ##
    def save_snmp_getnext(self,oid,result):
        self.snmp_getnext[oid]=result
    ## Save final result
    def save_result(self,result,motd=""):
        self.result=result
        self.motd=motd
    ## Dump canned data
    def dump(self,output):
        def format_stringdict(d):
            def lrepr(s):
                return repr(s)[1:-1]
            out=["{"]
            for k,v in d.items():
                lines=v.splitlines()
                if len(lines)<4:
                    out+=["%s:  %s,"%(repr(k),repr(v))]
                else:
                    out+=["## %s"%repr(k)]
                    out+=["%s: \"\"\"%s"%(repr(k),lrepr(lines[0]))]+[lrepr(l) for l in lines[1:-1]]+["%s\"\"\","%lrepr(lines[-1])]
            out+=["}"]
            return "\n".join(out)
        vendor,profile,script=self.script_name.split(".")
        date=str(datetime.datetime.now()).split(".")[0]
        s="""# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## %(script)s test
## Auto-generated by manage.py debug-script at %(date)s
##----------------------------------------------------------------------
## Copyright (C) 2007-%(year)d The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class %(test_name)s_Test(ScriptTestCase):
    script="%(script)s"
    vendor="%(vendor)s"
    platform='<<<INSERT YOUR PLATFORM HERE>>>'
    version='<<<INSERT YOUR VERSION HERE>>>'
    input=%(input)s
    result=%(result)s
    motd=%(motd)s
    cli=%(cli)s
    snmp_get=%(snmp_get)s
    snmp_getnext=%(snmp_getnext)s
"""%{
            "test_name"    : self.script_name.replace(".","_"),
            "script"       : self.script_name,
            "vendor"       : vendor,
            "year"         : datetime.datetime.now().year,
            "date"         : date,
            "input"        : pprint.pformat(self.input),
            "result"       : pprint.pformat(self.result),
            "cli"          : format_stringdict(self.cli),
            "snmp_get"     : pprint.pformat(self.snmp_get),
            "snmp_getnext" : pprint.pformat(self.snmp_getnext),
            "motd"         : pprint.pformat(self.motd),
        }
        with open(output,"w") as f:
            f.write(s)
##
## Activator emulation
##
class ActivatorStub(object):
    WAIT_TICKS=4
    def __init__(self,request,output=None):
        # Simple config stub
        self.config=ConfigParser.SafeConfigParser()
        self.config.read("etc/noc-activator.defaults")
        self.config.read("etc/noc-activator.conf")
        self.script_call_queue=Queue.Queue()
        self.ping_check_results=None
        self.factory=SocketFactory(tick_callback=self.tick)
        self.servers=ServersHub(self)
        self.log_cli_sessions=None
        self.wait_ticks=self.WAIT_TICKS
        self.to_save_output=output is not None
        self.output=output
        self.use_canned_session=False
        if self.to_save_output:
            self.script_name=request.script
            args={}
            for a in request.kwargs:
                args[a.key]=cPickle.loads(a.value)
            self.session_can=SessionCan(self.script_name,args)
    
    def tick(self):
        logging.debug("Tick")
        while not self.script_call_queue.empty():
            try:
                f,args,kwargs=self.script_call_queue.get_nowait()
            except:
                break
            logging.debug("Calling delayed %s(*%s,**%s)"%(f,args,kwargs))
            apply(f,args,kwargs)
        if len(self.factory.sockets)==0:
            self.wait_ticks-=1
            if self.wait_ticks==0:
                logging.debug("EXIT")
                if self.to_save_output:
                    logging.debug("Writing session test to %s"%self.output)
                    self.session_can.dump(self.output)
                os._exit(0)
            logging.debug("%d TICKS TO EXIT"%self.wait_ticks)
        else:
            self.wait_ticks=self.WAIT_TICKS
        
    def on_script_exit(self,script):
        if script.parent is None:
            self.servers.close()
        
    def run_script(self,_script_name,access_profile,callback,**kwargs):
        pv,pos,sn=_script_name.split(".",2)
        profile=profile_registry["%s.%s"%(pv,pos)]()
        script=script_registry[_script_name](profile,self,access_profile,**kwargs)
        script.start()
    
    def request_call(self,f,*args,**kwargs):
        logging.debug("Requesting call: %s(*%s,**%s)"%(f,args,kwargs))
        self.script_call_queue.put((f,args,kwargs))
    
    def can_run_script(self):
        return True
    ##
    ## Handler to accept canned input
    ##
    def save_interaction(self,provider,cmd,data):
        self.session_can.save_interaction(provider,cmd,data)
    ##
    ## Handler to save final result
    ##
    def save_result(self,result,motd=""):
        self.session_can.save_result(result,motd)
    ##
    def save_snmp_get(self,oid,result):
        self.session_can.save_snmp_get(oid,result)
    ##
    def save_snmp_getnext(self,oid,result):
        self.session_can.save_snmp_getnext(oid,result)

class Command(BaseCommand):
    help="Debug SA Script"
    option_list=BaseCommand.option_list+(
        make_option("-c","--read-community",dest="snmp_ro"),
        make_option("-o","--output",dest="output"),
    )
    def run_script(self,service,request):
        def handle_callback(controller,response=None,error=None):
            if error:
                logging.debug("Error: %s"%error.text)
            if response:
                logging.debug("Script completed")
                logging.debug(response.config)
        logging.debug("Running script thread")
        controller=Controller()
        tf=TransactionFactory()
        controller.transaction=tf.begin()
        service.script(controller=controller,request=request,done=handle_callback)
    
    def SIGINT(self,signo,frame):
        logging.info("SIGINT")
        os._exit(0)
    
    def set_access_profile_url(self,access_profile,url):
        url=URL(url)
        access_profile.scheme         = scheme_id[url.scheme]
        access_profile.address        = url.host
        if url.port:
            access_profile.port       = url.port
        access_profile.user           = url.user
        if "\x00" in url.password: # Check the password really the pair of password/enable password
            p,s=url.password.split("\x00",1)
            access_profile.password   = p
            access_profile.super_password = s
        else:
            access_profile.password   = url.password
        access_profile.path           = url.path
        return True
    
    def set_access_profile_name(self,access_profile,name):
        from noc.sa.models import ManagedObject
        from django.db.models import Q
        
        if is_int(name):
            q=Q(id=int(name))|Q(name=name)
        else:
            q=Q(name=name)
        try:
            o=ManagedObject.objects.get(q)
        except ManagedObject.DoesNotExist:
            return False
        access_profile.scheme = o.scheme
        access_profile.address= o.address
        if o.port:
            access_profile.port = o.port
        access_profile.user = o.user
        access_profile.password = o.password
        if o.super_password:
            access_profile.super_password=o.super_password
        if o.remote_path:
            access_profile.path=o.remote_path
        return True
    
    def set_access_profile(self,access_profile,arg):
        if "://" in arg:
            return self.set_access_profile_url(access_profile,arg)
        else:
            return self.set_access_profile_name(access_profile,arg)
        
    def handle(self, *args, **options):
        if len(args)<2:
            print "Usage: debug-script <script> (<stream url>|<object id>|<object_name>) [key1=value1 key2=value2 ... ]"
            print "Where value is valid python expression"
            return
        script_name=args[0]
        vendor,os_name,rest=script_name.split(".",2)
        profile_name="%s.%s"%(vendor,os_name)
        try:
            profile=profile_registry[profile_name]()
        except:
            print "Invalid profile. Available profiles are:"
            print "\n".join([x[0] for x in profile_registry.choices])
            return
        try:
            script_class=script_registry[script_name]
        except:
            print "Invalid script. Available scripts are:"
            print "\n".join([x[0] for x in script_registry.choices])
            return
        logging.root.setLevel(logging.DEBUG)
        signal.signal(signal.SIGINT,self.SIGINT)
        service=Service()
        r=ScriptRequest()
        r.script=script_name
        r.access_profile.profile        = profile_name
        if not self.set_access_profile(r.access_profile,args[1]):
            print "Invalid object name or url"
            return
        if options["snmp_ro"]:
            r.access_profile.snmp_ro=options["snmp_ro"]
        # Parse script args
        if len(args)>=3:
            for p in args[2:]:
                k,v=p.split("=",1)
                v=eval(v,{},{})
                a=r.kwargs.add()
                a.key=k
                a.value=cPickle.dumps(v)
        #
        service.activator=ActivatorStub(r,options.get("output",None))
        #
        t=threading.Thread(target=self.run_script,args=(service,r,))
        t.start()
        #
        service.activator.factory.run(run_forever=True)
