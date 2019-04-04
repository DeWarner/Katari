class SipObject:
    def __init__(self,sip_type=None,payload=None,parsed_data=None):
        self._sip_type = sip_type
        self._payload = payload
        self._parsed_data = parsed_data


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
