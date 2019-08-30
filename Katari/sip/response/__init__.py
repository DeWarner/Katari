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

    def create_response(self, message=None):
        try:
            self.set_via(mess)
            self.set_from(self._data["from"])
            self.set_to(self._data["to"])
            self.set_contact(self._data["contact"])
            self.set_call_id(self._data["call-id"])
            self.set_cseq(self._data["cseq"])
            return message
        except:
            return message
