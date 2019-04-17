"""
##    ##    ###    ########    ###    ########  ####
##   ##    ## ##      ##      ## ##   ##     ##  ##
##  ##    ##   ##     ##     ##   ##  ##     ##  ##
#####    ##     ##    ##    ##     ## ########   ##
##  ##   #########    ##    ######### ##   ##    ##
##   ##  ##     ##    ##    ##     ## ##    ##   ##
##    ## ##     ##    ##    ##     ## ##     ## ####

SIP (Session Initiated Protocol) Application Framework

"""
import logging
from Katari.server import SipServer
from Katari.logging import KatariLogging
from Katari.sip.response._4xx import MethodNotAllowed405
from Katari.sip.response import NullMessage
from Katari.errors import NoSettingsFound




class KatariApplication:




    def __init__(self,settings=None):
        self.loggerinit = KatariLogging()
        self.logger = logging.logging.getLogger(__name__)
        self._copy = False
        self.settings = settings
        self.send_q = None
        self.revc_q = None
        self.method_endpoint_register = {"INVITE":self.default_response,
                                         "ACK": self.null_response,
                                         "BYE": self.default_response,
                                         "CANCEL": self.default_response,
                                         "REGISTER": self.default_response,
                                         "OPTIONS": self.default_response,
                                         "PRACK": self.default_response,
                                         "SUBSCRIBE": self.default_response,
                                         "NOTIFY": self.default_response,
                                         "PUBLISH": self.default_response,
                                         "INFO": self.default_response,
                                         "REFER": self.default_response,
                                         "MESSAGE": self.default_response,
                                         "UPDATE": self.default_response}



    def register(self):
        def decorator(f):
            self.method_endpoint_register['REGISTER'] = f
            self
            return f
        return decorator

    def ack(self):
        def decorator(f):
            self.method_endpoint_register['ACK'] = f
            return f
        return decorator

    def cancel(self):
        def decorator(f):
            self.method_endpoint_register['CANCEL'] = f
            return f
        return decorator


    def invite(self):
        def decorator(f):
            self.method_endpoint_register['INVITE'] = f
            return f
        return decorator


    def options(self):
        def decorator(f):
            self.method_endpoint_register['OPTIONS'] = f
            return f
        return decorator

    def subscribe(self):
        def decorator(f):
            self.method_endpoint_register['SUBSCRIBE'] = f
            return f
        return decorator


    def run(self):
        server = self.start_server()


    def start_server(self):
        if self.settings['DEBUG']:
            self.logger.info("Starting Development Server on {}:{}".format(self.settings['PYSIP_HOST'], self.settings['PYSIP_PORT']))
        server = SipServer(self.settings['PYSIP_HOST'], self.settings['PYSIP_PORT'])
        server.register_app(self)
        server.start()


    def _server_run(self, message):
        print(message.sip_type)
        if message.sip_type == "REGISTER":
            return self.method_endpoint_register["REGISTER"](message)
        elif message.sip_type == "INVITE":
            return self.method_endpoint_register["INVITE"](message)
        elif message.sip_type == "ACK":
            return self.method_endpoint_register["ACK"](message)




    def default_response(self,request):
        return request.create_response(MethodNotAllowed405())

    def null_response(self, request):
        return request.create_response(NullMessage())

    def get_settings(self):
        pass

    def set_queues(self,send_q,recv_q):
        self.send_q = send_q
        self.revc_q = recv_q













