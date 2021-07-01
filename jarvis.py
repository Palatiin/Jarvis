# Jarvis - personal assistant, grandson of Tony Stark's Jarvis
# hopefully one day it will be at least as good as it's ancestor
# 29.6.2021
# Matus Remen (matus.remen4@gmail.com)

from sys import platform
import module_validator

class Jarvis:
    def __init__(self, modules_src: str = None):
        self.operating_system = platform
        self.modules = []           # list of loaded modules
        self.command_dict = {}      # list of commands which will run modules
        self.init_modules(modules_src)


    # loads all valid modules and their calling aliases
    def init_modules(self, src: str):
        if not src:
            src = "modules/"
        # default source directory is modules/
        available_modules = module_validator.load_modules(self.operating_system, src)

        for module_name in available_modules:
            class_str = module_name.title()
            import_str = f"from {src[:-1]}.{module_name}.{module_name} import {class_str}"
            init_str = f"module = {class_str}()"

            exec(import_str)
            exec(init_str)
            exec("self.modules.append(module)")

            # loading aliases
            if self.modules[-1].alias:
                self.command_dict.update({self.modules[-1].alias: self.modules[-1]})


    # loop where Jarvis waits for commands and executes them
    def listen(self):
        while 1:
            in_expression = input("$: ").split()
            
            if not in_expression:
                continue
           
            command = in_expression[0]
            module = self.command_dict.get(command)
            if module:
                module(in_expression[1:])
            elif command == "exit":
                break


if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.listen()

