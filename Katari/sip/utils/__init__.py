"""
Utils module containing all sip header classes
"""
import re
import logging
from collections import OrderedDict



class Message:
    """
    Base message
    """
    def __init__(self, message):
        self.raw_message = message
        self._data = OrderedDict()
        self.log = logging.getLogger('Katari')
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
        reg=re.compile('([a-zA-Z-]+:) ?(.*)')
        for header, value in dict(reg.findall(message)).items():
            try:
                print(header.lower())
                if header.lower() == "to:":
                    self._data[header.lower().replace(':','')] = URI(value)
                elif header.lower() == "from:":
                    self._data[header.lower().replace(':','')] = URI(value)
                elif header.lower() == "contact:":
                    self._data[header.lower().replace(':','')] = URI(value)
                else:
                    self._data[header.lower().replace(':','')] = value
            except Exception as err:
                self.log.exception(err)
                self.log.debug(header, value)

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
        self.log = logging.getLogger('Katari')
        self.uri = uri
        try:
            self.user = re.search("sip:(.*)@(.*)(?=;|:)", uri).group(1)
            self.address = re.search("sip:(.*)@(.*)(?=;|:)", uri).group(2)
        except Exception as err:
            self.log.exception(err)
            self.user = uri
            self.address = uri

    def __repr__(self):
        return self.uri

    def __str__(self):
        return str(self.uri)

    def get_address(self):
        return self.address

    def get_user(self):
        return self.user


class Allow:
    def __init__(self, values):
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


