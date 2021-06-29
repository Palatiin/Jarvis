# 29.6.2021

import os
import sys
import module_validator

class Jarvis:
    def __init__(self):
        self.modules = []
        self.command_list = []
        self.init_modules()


    def init_modules(self):
        available_modules = module_validator.load_modules()
        for module_name in available_modules:
            class_str = module_name.title()
            import_str = f"from modules.{module_name}.{module_name} import {class_str}"
            init_str = f"module = {class_str}()"
            exec(import_str)
            exec(init_str)
            exec("self.modules.append(module)")

            if self.modules[-1].alias:
                self.command_list.append(self.modules[-1].alias)

