class SipObject:
    def __init__(self,):
        self.sip_type = None
        self._payload = None
        self._parsed_data = None


    def get_to(self):
        try:
            return self._parsed_data['to']
        except KeyError:
            return None

    def get_from(self):
        try:
            return self._parsed_data['from']
        except KeyError:
            return None

    def get_via(self):
        try:
            return  self._parsed_data['via']
        except KeyError:
            return None


    def tostring(self):
        pass


