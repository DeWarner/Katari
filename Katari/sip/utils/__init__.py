from collections import OrderedDict
import re

class Message:

    def __init__(self, message):
        self.raw_message = message
        self._data = OrderedDict()
        if message != None:
            self.method_line, self.headers = message.decode().split('\r\n', 1)
            self._parser(self.headers)
            self.sip_type = self.get_method(self.method_line)


    def __getitem__(self, item):
        try:
            return self._data[item]
        except KeyError:
            return None


    def _parser(self, message):
         for line in message.split("\r\n"):
             try:
                  header, data = line.split(": ")
                  self._data[header.lower()] = data
             except Exception as e:
                 pass

    def get_method(self, methodline):
        try:
            return methodline.split()[0]
        except:
            pass


class SipURI:
    def __init__(self, message):
        """
        >>> a = SipURI("<sip:cal3254@192.234.1.12:5060;transport=udp>")
        >>> a.port
        5060
        >>> a.address
        'cal3254@192.234.1.12'
        >>> a.transport
        'udp'
        """
        self.address = re.search("sip:(.*)@(.*)(?=;)", message).group(0)

        #self.message = message
        #self.info = self.parse(message)
        #self.port = self.info.get("port")
        #self.transport = self.info.get("transport")
        #self.address = self.info.get("address")

    @staticmethod
    def parse(sip_message):
        """
        Takes in a sip message
        :param sip_message:
        :return: dict
        >>> a = SipURI.parse("<sip:cal3254@192.234.1.12:5060;transport=udp>")
        >>> a.get("port")
        5060
        >>> a.get("address")
        'cal3254@192.234.1.12'
        >>> a.get("transport")
        'udp'
        """
        message = sip_message[5:-1]
        # cal3254@192.234.1.12:5060;transport=udp
        if sip_message[:5] != "<sip:":
            raise Exception("tis not a sip message? :(")
        loc, tp = message.split(";")
        transport = tp.split("=")[1]
        address, port = loc.split(":")
        return dict(address=address, port=int(port), transport=transport)


class AllowType:
    def __init__(self):
        pass