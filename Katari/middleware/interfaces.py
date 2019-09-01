class MiddlewareInterface:
    
    def process_request(self):
        raise Exception("Must be implemented in child class")

    def process_response(self):
        raise Exception("Must be implemented in child class")