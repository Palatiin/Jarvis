from datetime import datetime
from preset import Preset
from time import sleep


class Time():
    def __init__(self):
        self.dateTime = str(datetime.now()).split()
        self.date = self.dateTime[0].split("-")[::-1]
        self.date[0], self.date[1] = self.date[1], self.date[0]
        self.date[0] = Preset.MONTHS[int(self.date[0])-1]
        self.dateStr = " ".join(self.date)
        self.time = self.dateTime[1][:self.dateTime[1].index(".")]

    def set_alarm(self, arg):
        if len(arg) == 8:
            self.set_alarm_thrd(arg)
        else:
            print("Time format error")
    def set_alarm_thrd(self, alarm_time):
        self.dateTime = str(datetime.now()).split()
        self.now = self.dateTime[1][:self.dateTime[1].index(".")]
        while self.now != alarm_time:
            sleep(1)
            self.now = datetime.now().strftime("%H:%M:%S")
        print('\a')
        print("It's the time")

