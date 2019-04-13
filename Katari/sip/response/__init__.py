from Katari.sip import SipMessage

class NullMessage(SipMessage):
    def __init__(self):
        super().__init__()
        self.sip_type = None
        self.method_line = ""