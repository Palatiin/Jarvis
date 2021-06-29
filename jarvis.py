# Jarvis - personal assistant, grandson of Tony Stark's Jarvis
# hopefully one day it will be at least as good as it's ancestor
# 29.6.2021
# Matus Remen (matus.remen4@gmail.com)

import os
import sys
import module_validator

class Jarvis:
    def __init__(self):
        self.modules = []           # list of loaded modules
        self.command_list = []      # list of commands which will run modules
        self.init_modules()


    # loads all valid modules and their calling aliases
    def init_modules(self):
        # default source directory is modules/
        available_modules = module_validator.load_modules()

        for module_name in available_modules:
            class_str = module_name.title()
            import_str = f"from modules.{module_name}.{module_name} import {class_str}"
            init_str = f"module = {class_str}()"
            
            exec(import_str)
            exec(init_str)
            exec("self.modules.append(module)")

            # loading aliases
            if self.modules[-1].alias:
                self.command_list.append(self.modules[-1].alias)

