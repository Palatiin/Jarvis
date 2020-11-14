class Preset:
    # TITLE/PATH
    JARVIS_BAR = '--> Jarvis'

    # 0> Win 1> Linux
    COMMAND_CLEAR = ["cls", "clear"]

    # EXIT
    EXIT_ALIASES = ["exit", ":q"]

    # BROWSER
    OPEN_LINK_COMMANDS = ["open", "about"]

    # NEWS MODULE
    NEWS_ALIASES = ["news"]
    NEWS_RELOAD_COMMANDS = ["rld", ["fit", "vut"]]
    NEWS_HELP = ["help",
                 '''
    This module drains newest information from FIT and VUT sites.
                  
     News in-module commands:
       - about/open/more [ID_of_info]  Opens page with more information,
       - rld [fit/vut/default=both]    Reloads news from one/both webs
       - exit                          Exits module /News''']

    # URLS
    URLS = {"fit": "https://www.fit.vut.cz/.cs",
            "vut": "https://www.vutbr.cz/",
            "google": "https://www.google.com/",
            "duck": "https://duckduckgo.com/",
            "yt": "https://www.youtube.com/"
            }

    # TIME
    TIME_ALIASES = ["time", "date"]
    TIME_COMMANDS = ["salarm"]
    # MONTHS
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
