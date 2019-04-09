from utils import Message
from Katari.sip import SipObject

class SipParser(SipObject):

    def __init__(self,sip_message):
        self._parse(sip_message)


    def __repr__(self):
        return "<{} Message instance at {}>".format(self.sip_type, hex(id(self)))


    def _parse(self, sip_message):
        """
        Takes in a sip message

        :param sip_message:
        :return:
        """

        self.parsed_data = Message(message=sip_message)
        self.payload = sip_message
        self.sip_type = self.parsed_data.sip_type


    def _get_message_type(self, message):
        return message.split()[0]















