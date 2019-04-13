import logging
import sys

class KatariLogging:

    def __init__(self):
       log = logging.basicConfig(stream=sys.stdout)


