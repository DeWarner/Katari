import logging
from logging.handlers import RotatingFileHandler


class KatariLogging:

    def __init__(self):
       self.log = logging.getLogger(__name__)
       self.log.setLevel(logging.INFO)
       self.handler = RotatingFileHandler("Katari.log",maxBytes=50 * 100000, backupCount=15)
       self.format_ = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
       self.handler.setFormatter(fmt=self.format_)
       self.log.addHandler(self.handler)


    def get_logger(self):
        return self.log



