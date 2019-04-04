class SipParser:

    @staticmethod
    def parse(sip_message):
        SipParser._get_message_type(sip_message)

    @staticmethod
    def _get_headers(message):
        for i in message:
            pass


    @staticmethod
    def _get_message_type(message):
        return message.split('\n',1)[0].split()[0]



    def




