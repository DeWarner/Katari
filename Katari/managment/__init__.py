import os
import pkgutil
import argparse
from importlib import import_module


class CommandParser:

    def __init__(self):
        #print os.path.join(os.path.dirname(__file__),"commands")
        self._load_commands()
        #parse = argparse.ArgumentParser(description='Katari Utility\'s')
        #parser.add_argument("create-app", help="Create katari application structure")
        #args = vars(parser.parse_args())

    def parse(self,command):
        pass

    def _load_commands(self):
        path = os.path.join(os.path.dirname(__file__), "commands")
        command_list = [command.replace(".py","") for command in os.listdir(path)
                        if not (command.startswith("_") or command.endswith(".pyc"))]

        for filtered_command in command_list:
            import_module("Katari.managment.commands." + filtered_command)




    def _find_commands(self):
        pass
        #return [for command in os.listdir(path)]




