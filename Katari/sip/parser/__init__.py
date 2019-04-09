from Katari.sip import SipMessage

class SipParser:

    def __init__(self,sip_message):
        self._parse(sip_message)


    def _parse(self, sip_message):
        """
        Takes in a sip message

        :param sip_message:
        :return:
        """

        self.parsed_data = SipMessage(message=sip_message)
        self.payload = sip_message
        self.sip_type = self.parsed_data.sip_type
















