class MiddlewareInterface:
    
    def process_request(self, message, client):
        return message, client

    def process_response(self, message, client):
        return message, client