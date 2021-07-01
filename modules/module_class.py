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
        self.name = None
        self.version = None
        self.platform = []
        self.author = None
        self.alias = ""             # calling command
        self.commands = {}          # command-method pairs
  
    ## call method of module, executes command in exp
    # @param exp command + arguments
    def __call__(self, exp: list):
        pass

    ## Prints help page of whole module or any of it's method
    def help(self, command: str = ""):
        pass
    
    def get_name(self):
        return self.name

    def get_version(self):
        return self.version
    
    def get_platform(self):
        return self.platform
    
    def get_author(self):
        return self.author

    def get_aliases(self):
        return self.aliases

