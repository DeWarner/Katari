import sys
import logging
from Katari.errors import UnKnownOutputMode
from logging.handlers import RotatingFileHandler


class KatariLogging:
    def __init__(self, filename="Katari.log", output_mode="file", level=logging.DEBUG):
        self.log = logging.getLogger('Katari')
        self.log.setLevel(level)
        if output_mode == 'file':
            self.handler = RotatingFileHandler(
                filename, maxBytes=50 * 100000, backupCount=15
            )
        elif output_mode == "stdout":
            self.handler = logging.StreamHandler(sys.stdout)
        else:
            raise UnKnownOutputMode(output_mode)
        self.format_ = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        self.handler.setFormatter(fmt=self.format_)
        self.log.addHandler(self.handler)

    def get_logger(self):
        return self.log
