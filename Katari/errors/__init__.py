class NoBaseCommandClass(Exception):
    pass


class NoSettingsFound(Exception):
    pass

class UnKnownOutputMode(Exception):

    def __init__(self, output_mode):
        super().__init__("Unknown output mode {}, please check settings.py".format(output_mode))


