from Katari.sip import SipMessage


class MultipleChoices300(SipMessage):
    def __init__(self):
        super().__init__()
        self.method_line = "SIP/2.0 300 Multiple Choices\r\n"


class MovedPermanently301(SipMessage):
    def __init__(self):
        pass


class MovedTemporarily302(SipMessage):
    def __init__(self):
        super().__init__()
        self.method_line = "SIP/2.0 302 Moved Temporarily\r\n"


class UseProxy305(SipMessage):
    def __init__(self):
        pass


class AlternativeService380(SipMessage):
    def __init__(self):
        pass
