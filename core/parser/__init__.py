from mimetools import Message
from StringIO import StringIO

class SipParser:

    @staticmethod
    def parse(sip_message):

        request_line, headers_alone = sip_message.split('\r\n', 1)
        return Message(StringIO(headers_alone))

    @staticmethod
    def _get_message_type(message):
        return message.split('\n',1)[0].split()[0]








