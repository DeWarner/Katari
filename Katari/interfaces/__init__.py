class MiddlewareInterface:
    
    def process_request(self, message, client):
        return message

    def process_response(self, message, client):
        return message