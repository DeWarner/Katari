from .utils import Message

class SipMessage(Message):
    def __init__(self,message=None):
        super().__init__(message=message)
        self.sip_type = None
        self._payload = None
        self._data = None
        self.to = None
        self.from_ = None
        self.via = None
        self.call_id = None
        self.contact = None
        self.allow = None


    def get_to(self):
        try:
            return self._data['to']
        except KeyError:
            return None

    def get_from(self):
        try:
            return self._data['from']
        except KeyError:
            return None

    def get_via(self):
        try:
            return  self._data['via']
        except KeyError:
            return None

    def set_via(self, via):
        self.via = via

    def set_from(self, from_):
        self.from_ = from_

    def set_to(self, to):
        self.to = to

    def set_contact(self, contact):
        self.contact = contact

    def set_call_id(self, call_id):
        self.call_id = call_id

    def set_allow(self, allow):
        self.allow = allow

    def set_message_type(self, message_type):
        self.sip_type = message_type


    def tostring(self):
        pass


