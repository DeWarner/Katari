from Katari.sip import SipMessage

class SipParser:

    def __init__(self,sip_message):
        return self._parse(sip_message)


    def _parse(self, sip_message):
        """
        Takes in a sip message

        :param sip_message:
        :return:
        """

        return SipMessage(message=sip_message)
















