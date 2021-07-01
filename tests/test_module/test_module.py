# 29.6.2021

from modules.module_class import Module

class Test_Module(Module):
    def __init__(self):
        super().__init__()
        self.name = "Test Module"
        self.version = "1.0"
        self.platform = ["linux"]
        self.author = "Matus"
        self.alias = "test"
        self.commands = {}

