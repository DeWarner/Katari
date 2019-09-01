import importlib

class MiddlewareLoader:

    def __init__(self, middleware=None):
        self.middleware = middleware

    def load(self):
        """ Takes list and imports middleware """
        for _m in self.middleware:
            importlib.import_module(_m)