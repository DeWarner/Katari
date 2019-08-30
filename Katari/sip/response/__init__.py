from Katari.sip import SipMessage


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
