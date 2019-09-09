from Katari.sip import SipMessage


class OK200(SipMessage):
    def __init__(self):
        super().__init__()
        self.method_line = "SIP/2.0 200 OK\r\n"


class Accepted202(SipMessage):
    def __init__(self):
        super().__init__()
        self.method_line = "SIP/2.0 202 Accepted\r\n"


class NoNotification204(SipMessage):
    def __init__(self):
        super().__init__()
        pass
