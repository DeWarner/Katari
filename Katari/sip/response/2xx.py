from Katari.sip import SipMessage

class OK200(SipMessage):
    def __init__(self,request):
        pass

class Accepted202(SipMessage):
    def __init__(self):
        pass

class NoNotification204(SipMessage):
    def __init__(self):
        pass