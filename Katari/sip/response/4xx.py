from Katari.sip import SipMessage


class BadRequest400(SipMessage):
    def __init__(self):
        pass

class Unauthorized401(SipMessage):
    def __init__(self):
        pass

class PaymentRequired402(SipMessage):
    def __init__(self):
        pass

class Forbidden403(SipMessage):
    def __init__(self):
        pass

class NotFound404(SipMessage):
    def __init__(self):
        pass

class MethodNotAllowed405(SipMessage):
    def __init__(self):
        pass

class NotAcceptable406(SipMessage):
    def __init__(self):
        pass

class ProxyAuthenticationRequired407(SipMessage):
    def __init__(self):
        pass