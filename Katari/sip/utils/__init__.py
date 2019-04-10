from collections import OrderedDict

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
                 pass  #TODO - Return 400 bad request

    def get_method(self, methodline):
        try:
            return methodline.split()[0]
        except:
            pass







class URI:
    def __init__(self,uri):
        pass


class AllowType:
    def __init__(self):
        pass