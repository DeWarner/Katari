class SipURI:
    def __init__(self, message):
        """
        >>> a = SipURI("<sip:cal3254@192.234.1.12:5060;transport=udp>")
        >>> (a.port, a.address, a.transport)
        (5060, 'cal3254@192.234.1.12', 'udp')
        """
        self.message = message
        self.info = self.parse(message)
        self.port = self.info.get("port")
        self.transport = self.info.get("transport")
        self.address = self.info.get("address")

    @staticmethod
    def parse(sip_message):
        """
        Takes in a sip URI header,
        returns a dict of properties that could be deduced.
        :return: dict
        >>> a = SipURI.parse("<sip:cal3254@192.234.1.12:5060;transport=udp>")
        >>> (a.get("port"), a.get("address"), a.get("transport"))
        (5060, 'cal3254@192.234.1.12', 'udp')
        """
        message = sip_message[5:-1]
        # cal3254@192.234.1.12:5060;transport=udp
        if sip_message[:5] != "<sip:":
            raise Exception("tis not a sip message? :(")
        location_information, transport_item = message.split(";")
        transport = transport_item.split("=")[1]
        address, port = location_information.split(":")
        return dict(address=address, port=int(port), transport=transport)
