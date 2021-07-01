# 1.7.2021

from modules.module_class import Module
from datetime import datetime

class Time(Module):
    def __init__(self):
        super().__init__()
        self.name = "Time Module"
        self.version = "0.0.0"
        self.platform = ["linux"]
        self.author = "Matus"
        self.alias = "time"
        self.commands = {}

    def __call__(self, attributes: list):
        if len(attributes) == 0:
            print("time/$: " + self.get_time())

    def get_time(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

