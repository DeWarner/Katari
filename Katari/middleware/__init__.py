import sys
import importlib
import logging
import inspect

class MiddlewareLoader:

    def __init__(self, middleware=None):
        self.middleware = middleware
        self.log = logging.getLogger(__name__)
        

    def load(self):
        """ Takes list and imports middleware """

        middleware_array = []

        for _module in self.middleware:
            mod = importlib.import_module(_module)
            _class = getattr(mod, str(inspect.getmembers(sys.modules[_module], inspect.isclass)[0][0]))
            middleware_array.append(_class())
            self.log.info("Middleware {} Loaded".format(mod.__name__))
        return middleware_array
            