"""
>>> a = ParsedMessage.parse("<sip:cal3254@192.234.1.12:5060;transport=udp>")
>>> a.get("port")
5060
>>> a.get("address")
'cal3254@192.234.1.12'
>>> a.get("transport")
'udp'
"""
from Katari.sip import SipMessage


class ParsedMessage:
    def __init__(self, message):
        self.message = message
        self.info = self.parse(message)
        self.port = info.get("port")
        self.transport = info.get("transport")
        self.address = info.get("address")
        

    @staticmethod
    def parse(sip_message):
        """
        Takes in a sip message
        :param sip_message:
        :return: dict
        """
        message = sip_message[5:-1]
        # cal3254@192.234.1.12:5060;transport=udp
        if sip_message[:5] != "<sip:":
            raise Exception("tis not a sip message? :(")
        loc, tp = message.split(";")
        transport = tp.split("=")[1]
        address, port = loc.split(":")
        return dict(address=address, port=int(port), transport=transport)
