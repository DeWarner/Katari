from Katari.interfaces import MiddlewareInterface


class SessionHandler(MiddlewareInterface):

    def __init__(self):
        pass
        
    def process_request(self, message):
        return message

    def process_response(self, response):
        return response
        


