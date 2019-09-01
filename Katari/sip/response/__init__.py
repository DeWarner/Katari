from Katari.sip import SipMessage
from Katari.sip.response._1xx import *
from Katari.sip.response._2xx import *
from Katari.sip.response._3xx import *
from Katari.sip.response._4xx import *



class ResponseFactory:

    @staticmethod
    def build(code):
        if code == 100:
            return Trying100()
        elif code == 180:
            return Ringing180()
        elif code == 181:
            return CallisBeingForwarded181()
        elif code == 182:
            return Queued182
        elif code == 183:
            return SessionProgress183()
        elif code == 199:
            return EarlyDialogTerminated199()
        elif code == 200:
            return OK200()
        elif code == 202:
            return Accepted202()
        elif code == 204:
            return NoNotification204()
        elif code == 300:
            return MultipleChoices300()
        elif code == 301:
            return MovedPermanently301()
        elif code == 302:
            return MovedTemporarily302()
        elif code == 305:
            return UseProxy305()
        elif code == 380:
            return AlternativeService380()
        elif code == 400:
            return BadRequest400()
        elif code == 401:
            return Unauthorized401()
        elif code == 402:
            return PaymentRequired402()
        elif code == 403:
            return Forbidden403()
        elif code == 404:
            return NotFound404()
        elif code == 405:
            return MethodNotAllowed405()
        elif code == 406:
            return NotAcceptable406()
        elif code == 407:
            return ProxyAuthenticationRequired407()
        else:
            return None
        


class NullMessage(SipMessage):
    def __init__(self):
        super().__init__()
        self.sip_type = None
        self.method_line = ""


class Ack(SipMessage):
    def __init__(self):
        super().__init__()
        self.sip_type = None
        self.method_line = "ACK {} SIP/2.0\r\n"
