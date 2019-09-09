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
import sys
from Katari.server.udp import UDPSipServer
from Katari.logging import KatariLogging
from Katari.sip import SipMessage
from Katari.sip.response._4xx import MethodNotAllowed405
from Katari.sip.response import NullMessage, Ack
from Katari.errors import NoSettingsFound
from Katari.middleware import MiddlewareLoader


class KatariApplication(UDPSipServer):
    """
    Katari instance is the main
    """
    def __init__(self, settings=None):
        # Loads default settings
        if not settings:
            from Katari.template import settings
            self.settings = settings
        else:
            self.settings = settings


        UDPSipServer.settings = settings

        self.loggerinit = KatariLogging(filename=self.settings.KATARI_LOGGING['LOGFILE'], output_mode=self.settings.KATARI_LOGGING['OUTPUTMODE'])
        self.logger = self.loggerinit.get_logger()
        self._copy = False
        self.socket = None
        self.client = None

        self.middleware_array = None

        self.load_middleware()

        self.method_endpoint_register = {
            "INVITE": self.default_response,
            "ACK": self.null_response,
            "BYE": self.default_response,
            "CANCEL": self.ack,
            "REGISTER": self.default_response,
            "OPTIONS": self.default_response,
            "PRACK": self.default_response,
            "SUBSCRIBE": self.default_response,
            "NOTIFY": self.default_response,
            "PUBLISH": self.default_response,
            "INFO": self.default_response,
            "REFER": self.default_response,
            "MESSAGE": self.default_response,
            "UPDATE": self.default_response,
            "RESPONSE": self.default_response,
        }

    def register(self):
        def decorator(f):
            self.method_endpoint_register["REGISTER"] = f
            return f
        return decorator

    def ack(self):
        def decorator(f):
            self.method_endpoint_register["ACK"] = f
            return f

        return decorator

    def cancel(self):
        def decorator(f):
            self.method_endpoint_register["CANCEL"] = f
            return f

        return decorator

    def invite(self):
        def decorator(f):
            self.method_endpoint_register["INVITE"] = f
            return f

        return decorator

    def options(self):
        def decorator(f):
            self.method_endpoint_register["OPTIONS"] = f
            return f

        return decorator

    def subscribe(self):
        def decorator(f):
            self.method_endpoint_register["SUBSCRIBE"] = f
            return f

        return decorator

    def info(self):
        def decorator(f):
            self.method_endpoint_register["INFO"] = f
            return f

        return decorator


    def status_response(self):
        def decorator(f):
            self.method_endpoint_register["RESPONSE"] = f
            return f
        return decorator


    def run(self):
        try:
            self.logger.info(
                "Starting Server on {}:{}".format(
                    self.settings.HOST, self.settings.PORT
                )
            )
            KatariApplication.start(
                (self.settings.HOST, self.settings.PORT), self
            )
        except KeyboardInterrupt:
            self.logger.info("Stopping Server")
            sys.exit()

    def _server_run(self, message, client):
        message, client = self.run_middleware_request(message, client)
        if message.sip_type == "REGISTER":
            try:
                self.logger.info(
                    "Received REGISTER request from {} ".format(client[0])
                )
                self.logger.debug("\n\n" + message.export())
                self.method_endpoint_register["REGISTER"](message, client)
            except Exception as err:
                self.logger.error(err)
        elif message.sip_type == "INVITE":
            try:
                self.logger.info("Received INVITE from {} ".format(client[0]))
                self.logger.debug("\n\n" + message.export())
                self.method_endpoint_register["INVITE"](message, client)
            except Exception as err:
                self.logger.error(err)
        elif message.sip_type == "OPTIONS":
            try:
                self.logger.info("Received OPTIONS from {} ".format(client[0]))
                self.logger.debug("\n\n" + message.export())
                self.method_endpoint_register["OPTIONS"](message, client)
            except Exception as err:
                self.logger.error(err)
        elif message.sip_type == "CANCEL":
            try:
                self.logger.info("Received CANCEL from {} ".format(client[0]))
                self.logger.debug("\n\n" + message.export())
                self.method_endpoint_register["CANCEL"](message, client)
            except Exception as err:
                self.logger.error(err)
        elif message.sip_type == "ACK":
            self.logger.info("Received Ack from {} ".format(client[0]))
        else:
            try:
                self.logger.info("Received response from {} ".format(client[0]))
                self.logger.debug("\n\n" + message.export())
                self.method_endpoint_register["RESPONSE"](message, client)
            except Exception as err:
                self.logger.error(err)

    def default_response(self, request, client):
        self.send(request.create_response(MethodNotAllowed405()), client)

    def null_response(self, request):
        return request.create_response(NullMessage())

    def send(self, message, client):
        """ Middleware execution """
        message, client = self.run_middleware_response(message, client)
        self.logger.info("Sending response to {} ".format(client[0]))
        self.logger.debug("\n\n" + message.export())
        self.socket[1].sendto(message.export().encode(), client)

    def receive(self):
        return SipMessage(self.rfile.read())

    def run_middleware_request(self, message, client):
        for _m in self.middleware_array:
            self.logger.debug("running request middleware layer {}".format(_m))
            message, client = _m.process_request(message, client)
        return message , client

    def run_middleware_response(self, message, client):
        for _m in self.middleware_array:
            self.logger.debug("running response middleware layer {}".format(_m))
            message, client = _m.process_response(message, client)
        return message, client

    def load_middleware(self):
        try:
            self.middleware_array = MiddlewareLoader(self.settings.KATARI_MIDDLEWARE).load()
        except ModuleNotFoundError as err:
            self.logger.error("No middleware called {}".format(str(err).split(" ")[3]))
            sys.exit(1)
           
        

