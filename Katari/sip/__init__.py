import logging
from Katari.sip.utils import Message, URI


class SipMessage(Message):
    def __init__(self, message=None):
        super().__init__(message=message)
        self._payload = None
        self.log = logging.getLogger('Katari')

    def get_to(self):
        try:
            return self._data["to"]
        except KeyError:
            return None

    def get_from(self):
        try:
            return self._data["from"]
        except KeyError:
            return None

    def get_via(self):
        try:
            return self._data["via"]
        except KeyError:
            return None
        
    def get_contact(self):
        try:
            return self._data['contact']
        except:
            return None
    
    def get_call_id(self):
        try:
            return self._data['call-id']
        except KeyError:
            return None
    
    def get_allow(self):
        try:
            return self._data['allow']
        except KeyError:
            return None
    
    def get_cseq(self):
        try:
            return self._data['cseq']
        except KeyError:
            return None

    def get_message_type(self):
        try:
            return self.sip_type
        except KeyError:
            return None

    def get_content_length(self):
        try:
            self._data["content-length"]
        except:
            return None

    def set_via(self, via):
        self._data["via"] = via

    def set_from(self, from_):
        self._data["from"] = from_

    def set_to(self, to):
        self._data["to"] = to

    def set_contact(self, contact):
        self._data["contact"] = contact

    def set_call_id(self, call_id):
        self._data["call-id"] = call_id

    def set_allow(self, allow):
        self._data["allow"] = allow

    def set_cseq(self, cseq):
        self._data["cseq"] = cseq

    def set_message_type(self, message_type):
        self.sip_type = message_type

    def set_content_length(self, content_length):
        self._data["content-length"] = content_length

    def export(self):
        message = ""
        message = message + self.method_line
        for k, v in self._data.items():
            value = str(v).replace('\r\n','')
            value = value.replace('\r','')
            line = k.capitalize() + ": " + value + "\r\n"
            message = message + line 
        message = message + "\r\n\r\n"
        return message

    def create_response(self, message=None):
        try:
            message.set_via(self._data['via'])
        except KeyError:
            self.log.debug("Via Header not in request")
        try:
            message.set_from(self._data['from'])
        except KeyError:
            self.log.debug("From Header not in request")
        try:
            message.set_to(self._data['to'])
        except KeyError :
            self.log.debug("To Header not in request")
        try:
            message.set_contact(self._data['contact'])
        except KeyError:
            self.log.debug("Contact Header not in request")
        try:
            message.set_call_id(self._data['call-id'])
        except KeyError:
            self.log.debug("Call-ID Header not in request")
        try:
            message.set_cseq(self._data['cseq'])
        except KeyError:
            self.log.exception("CSeq Header not in request")
        try:
            message.set_content_length(self._data['content-length'])
        except KeyError:
            self.log.exception("Content-Length Header not in request")
        return message
        