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
from Katari.server import SipServer



class SipApplication:




    def __init__(self):
        self._copy = False
        self.config = {"PYSIP_HOST":"127.0.0.1",
                       "PYSIP_PORT": 5060,
                       "PYSIP_BACKEND": None,
                       "PROTOCOL": None,
                       "DEBUG": True
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

    def ack(self):
        def decorator(f):
            self.method_endpoint_register['ACK'] = f
            return f
        return decorator

    def bye(self):
        def decorator(f):
            self.method_endpoint_register['BYE'] = f
            return f
        return decorator

    def cancel(self):
        def decorator(f):
            self.method_endpoint_register['CANCEL'] = f
            return f
        return decorator

    def options(self):
        def decorator(f):
            self.method_endpoint_register['OPTIONS'] = f
            return f
        return decorator

    def prack(self):
        def decorator(f):
            self.method_endpoint_register['PRACK'] = f
            return f
        return decorator

    def subscribe(self):
        def decorator(f):
            self.method_endpoint_register['SUBSCRIBE'] = f
            return f
        return decorator

    def notify(self):
        def decorator(f):
            self.method_endpoint_register['NOTIFY'] = f
            return f
        return decorator

    def publish(self):
        def decorator(f):
            self.method_endpoint_register['PUBLISH'] = f
            return f
        return decorator

    def info(self):
        def decorator(f):
            self.method_endpoint_register['INFO'] = f
            return f
        return decorator

    def refrer(self):
        def decorator(f):
            self.method_endpoint_register['REFER'] = f
            return f
        return decorator

    def update(self):
        def decorator(f):
            self.method_endpoint_register['REFER'] = f
            return f
        return decorator


    def run(self):
        server = self.start_server()




    def start_server(self):
        if self.config['DEBUG']:
            print "Starting Development Server on {}:{}".format(self.config['PYSIP_HOST'], self.config['PYSIP_PORT'])
        server = SipServer(self.config['PYSIP_HOST'], self.config['PYSIP_PORT'])
        server.register_app(self)
        server.start()


    def _server_run(self, message):
        if message.sip_type == "REGISTER":
            self.method_endpoint_register["REGISTER"](message)











