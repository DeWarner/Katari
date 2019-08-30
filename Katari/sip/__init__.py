from Katari.sip.utils import Message, URI


class SipMessage(Message):
    def __init__(self, message=None):
        super().__init__(message=message)
        self._payload = None

    def get_to(self):
        try:
            return URI(self._data["to"])
        except KeyError:
            return None

    def get_from(self):
        try:
            return SipURI(self._data["from"])
        except KeyError:
            return None

    def get_via(self):
        try:
            return self._data["via"]
        except KeyError:
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

    def export(self):
        message = ""
        message = message + self.method_line
        for k, v in self._data.items():
            line = k.capitalize() + ": " + v
            message = message + line + "\r\n"
        message = message + "\r\n"
        return message

    def create_response(self, message=None):
        try:
            self.set_via(message["via"])
            self.set_from(message["from"])
            self.set_to(message["to"])
            self.set_contact(message["contact"])
            self.set_call_id(message["call-id"])
            self.set_cseq(message["cseq"])
            return self.export()
        except Exception as e:
            return self.export()