import os
import sys
import pkgutil
import argparse
import logging
from importlib import import_module
from Katari.logging import KatariLogging
from Katari.errors import NoBaseCommandClass


class CommandParser:

    def __init__(self):
        self.logger = KatariLogging().get_logger()
        self._load_commands()

    def parse(self,command):
        pass

    def _load_commands(self):
        """
        loads/imports all commands from the commands submodule, works as a "plugin"
        :return:
        """
        path = os.path.join(os.path.dirname(__file__), "commands")
        command_list = [command.replace(".py","") for command in os.listdir(path)
                        if not (command.startswith("_") or command.endswith(".pyc"))]

        for filtered_command in command_list:
            import_module("Katari.managment.commands." + filtered_command)
            self._register_command(
                "Katari.managment.commands." + filtered_command)


    def _find_commands(self):
        pass
        #return [for command in os.listdir(path)]


    def _register_command(self,command_loc):
        """
        Registers command matched with command name derived from said command class

        :param command_loc:
        :return:
        """
        self.logger.info("Registering {}".format(command_loc))
        self._validate_command(dir(sys.modules[command_loc]))




    def _validate_command(self, classes):
        """
        Checks if command has BaseCommand as a parent

        :param classes:
        :return:
        """
        if "BaseCommand" in classes:
            return True
        raise NoBaseCommandClass("No Base Class Detected")

