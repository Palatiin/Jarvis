"""
Module: Module Example
Version: 1.0
Platform: Linux
Aliases: test
Commands:
Author: Matus
"""
# 29.6.2021
# pattern for all modules

## Parent class for all module classes
#  version, platform, name and aliases must not be empty
class Module:
    def __init__(self):
        self.author = None
        self.version = None
        self.platform = None
        self.name = None
        self.aliases = []           # calling commands
        self.commands = {}          # command-method pairs
    
    ## Prints help page of whole module or any of it's method
    def help(self, command: str = ""):
        pass

    def get_author(self):
        return self.author

    def get_version(self):
        return self.version

    def get_platform(self):
        return self.platform

    def get_name(self):
        return self.name

    def get_aliases(self):
        return self.aliases

