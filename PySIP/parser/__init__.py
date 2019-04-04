from mimetools import Message
from StringIO import StringIO

class SipParser:

    @staticmethod
    def parse(sip_message):
        request_line, headers_alone = sip_message.split('\r\n', 1)
        type = SipParser._get_message_type(request_line)
        return Message(StringIO(headers_alone))

    @staticmethod
    def _get_message_type(message):
        return message.split()[0]


    @staticmethod
    def _create_sip_object():
        pass









