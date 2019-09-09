from Katari.sip import SipMessage


class Trying100(SipMessage):
    def __init__(self):
        super().__init__()
        self.method_line = "SIP/2.0 100 Trying\r\n"


class Ringing180(SipMessage):
    def __init__(self):
        super().__init__()
        self.method_line = "SIP/2.0 180 Ringing\r\n"


class CallisBeingForwarded181:
    def __init__(self):
        pass


class Queued182(SipMessage):
    def __init__(self):
        super().__init__()
        self.method_line = "SIP/2.0 182 Queued\r\n"


class SessionProgress183(SipMessage):
    def __init__(self):
        super().__init__()
        self.method_line = "SIP/2.0 183 Session Progress\r\n"


class EarlyDialogTerminated199:
    def __init__(self):
        pass
