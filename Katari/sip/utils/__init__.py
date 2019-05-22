"""
Utils module containing all sip header classes
"""
from collections import OrderedDict
import re


class Message:
    """
    Base message
    """
    def __init__(self, message):
        self.raw_message = message
        self._data = OrderedDict()
        if message:
            self.method_line, self.headers = message.decode().split("\r\n", 1)
            self._parser(self.headers)
            self.sip_type = self.get_method(self.method_line)

    def __getitem__(self, item):
        """
        :param item:
        :return:
        """
        try:
            return self._data[item]
        except KeyError:
            return None

    def _parser(self, message):
        """
        :param message:
        :return:
        """
        for line in message.split("\r\n"):
            try:
                header, data = line.split(": ")
                self._data[header.lower()] = data
            except Exception as err:
                pass

    def get_method(self, methodline):
        """
        :param methodline:
        :return:
        """
        try:
            return methodline.split()[0]
        except:
            pass


class URI:
    """

    """
    def __init__(self, uri):
        self.uri = uri
        self.address = re.search("sip:(.*)@(.*)(?=;)", uri).group(0)
        self.user = re.search("sip:(.*)@(.*)(?=;)", uri).group(1)

    def __repr__(self) :
        return self.uri

    def get_address(self):
        return self.address

    def get_user(self):
        return self.user


class Allow:
    def __init__(self):
        pass

class Via:
    def __init__(self):
        pass

class CallId:
    def __init__(self):
        pass

class From:
    def __init__(self):
        pass

class To:
    def __init__(self):
        pass


