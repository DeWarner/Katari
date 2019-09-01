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

        for _m in self.middleware:
            mod = importlib.import_module(_m)
            klass = inspect.getmembers(sys.modules[_m], inspect.isclass)
            newklass = getattr(mod, str(klass[1][0]))
            middleware_array.append(newklass())
            self.log.info("Middleware {} Loaded".format(mod.__name__))
        return middleware_array
            