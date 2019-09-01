class MiddlewareInterface:
    
    def process_request(self, message):
        return message

    def process_response(self, message):
        return message