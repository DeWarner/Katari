"""
########  ##    ##  ######  #### ########
##     ##  ##  ##  ##    ##  ##  ##     ##
##     ##   ####   ##        ##  ##     ##
########     ##     ######   ##  ########
##           ##          ##  ##  ##
##           ##    ##    ##  ##  ##
##           ##     ######  #### ##

Python SIP (Session Initiated Protocol) Application Framework

"""
import logging
from Katari.server import SipServer
from Katari.logging import KatariLogging




class KatariApplication:




    def __init__(self):
        self.loggerinit = KatariLogging()
        self.logger = logging.logging.getLogger(__name__)
        self._copy = False
        self.config = {"PYSIP_HOST":"127.0.0.1",
                       "PYSIP_PORT": 5060,
                       "PYSIP_BACKEND": None,
                       "PROTOCOL": None,
                       "DEBUG": True,
                       "LOGGING": ""
                       }

        self.method_endpoint_register = {"INVITE":None,
                                         "ACK": None,
                                         "BYE": None,
                                         "CANCEL": None,
                                         "REGISTER": None,
                                         "OPTIONS": None,
                                         "PRACK": None,
                                         "SUBSCRIBE": None,
                                         "NOTIFY": None,
                                         "PUBLISH": None,
                                         "INFO": None,
                                         "REFER": None,
                                         "MESSAGE": None,
                                         "UPDATE": None}


    def register(self):
        def decorator(f):
            self.method_endpoint_register['REGISTER'] = f
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
        if self.config['DEBUG']:
            self.logger.info("Starting Development Server on {}:{}".format(self.config['PYSIP_HOST'], self.config['PYSIP_PORT']))
        server = SipServer(self.config['PYSIP_HOST'], self.config['PYSIP_PORT'])
        server.register_app(self)
        server.start()


    def _server_run(self, message):
        if message.sip_type == "REGISTER":
            return self.method_endpoint_register["REGISTER"](message)
        return message











