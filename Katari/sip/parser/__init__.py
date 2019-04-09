from rfc822 import Message
from StringIO import StringIO
from Katari.sip import SipObject

class SipParser(SipObject):

    def __init__(self,sip_message):
        self._parse(sip_message)


    def __repr__(self):
        return "<{} Message instance at {}>".format(self.sip_type, hex(id(self)))


    def _parse(self, sip_message):
        """
        Takes in a sip message and
        :param sip_message:
        :return:
        """
        request_line, headers_alone = sip_message.split('\r\n', 1)
        self.sip_type = self._get_message_type(request_line)
        self.parsed_data = Message(StringIO(headers_alone))
        self.payload = sip_message


    def _get_message_type(self, message):
        return message.split()[0]















