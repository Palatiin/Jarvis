# mts - *9.9.2020

import os
from platform import system
from preset import Preset
from time import sleep
from modules.news import News
from modules.browser import Browser


# TODO: differ WIN from UNIX --HIGH PRIORITY - Preset.COMMAND_CLEAR[0/1] win/lnx,
# TODO: unix speaker

O_SYSTEM = 0 if system() == "Windows" else 1

os.system(Preset.COMMAND_CLEAR[O_SYSTEM])
print(f"@{system()}")
print(
    '''
    ▄▄▄▄▄▄▄    ▄▄▄    ▄▄▄▄▄    ▄     ▄  ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          █   █   █   █    █   █     █    ▐█▌    █     ▀
          █   █   █   █     █  █     █    ▐█▌    █
          █  █     █  █▄▄▄▄▀    █   █     ▐█▌     ▀▀▀▀▄
          █  █▄▄▄▄▄█  █   █     █   █     ▐█▌          █
    ▄     █  █     █  █    █     ▌ ▐      ▐█▌    ▄     █
     ▀▄▄▄▀   █     █  █     █     █     ▄▄███▄▄   ▀▄▄▄▀
    '''
)

while True:
    command = list(input().split())
    try:
        if command[0] in Preset.EXIT_ALIASES:
            print("See you next time.")
            sleep(.7)
            break
        elif command[0] in Preset.NEWS_ALIASES:
            if len(command) > 1:
                News(command[1])
                os.system(Preset.COMMAND_CLEAR[O_SYSTEM])
                print(Preset.JARVIS_BAR)
            else:
                News()
                os.system(Preset.COMMAND_CLEAR[O_SYSTEM])
                print(Preset.JARVIS_BAR)
        elif command[0] in Preset.OPEN_LINK_COMMANDS:
            if len(command) > 1:
                if '.' in command[1]:
                    Browser(command[1])
                elif command[1] in Preset.URLS.keys():
                    Browser(Preset.URLS[command[1]])
                else:
                    print("Incorect format or unknown page.")
            else:
                Browser()
        else:
            print("I don't know that command..")
    except IndexError:
        pass
