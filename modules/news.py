# mts - *9.9.2020

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from preset import Preset
from modules.browser import Browser


class News(object):
    def __init__(self, site: str = "both"):
        print(Preset.JARVIS_BAR + "/News")

        self.aim = site
        self.data = [[], []]
        if self.aim in ["both", "all", 'a']:
            self.data[0], self.data[1] = self.get_fitnews(), self.get_vutnews()
            self.print_news(self.data)
        elif self.aim in ["fit", 'f']:
            self.data[0] = self.get_fitnews()
            self.print_news(self.data)
        elif self.aim in ["vut", 'v']:
            self.data[1] = self.get_vutnews()
            self.print_news(self.data)

        # handling in-module commands
        while True:
            self.command = list(input().split())
            try:
                if self.command[0] in Preset.EXIT_ALIASES:
                    break

                elif self.command[0] == Preset.NEWS_HELP[0]:
                    print(Preset.NEWS_HELP[1])

                elif self.command[0] == Preset.NEWS_RELOAD_COMMANDS[0]:
                    if len(self.command) > 1:
                        if self.command[1] == Preset.NEWS_RELOAD_COMMANDS[1][0]:
                            self.data[0] = self.get_fitnews()
                            self.print_news(self.data[:1])
                        elif self.command[1] == Preset.NEWS_RELOAD_COMMANDS[1][1]:
                            self.data[1] = self.get_vutnews()
                            self.print_news(self.data[1:])
                        else:
                            print("I can't access these news.")
                    else:
                        self.data[0], self.data[1] = self.get_fitnews(), self.get_vutnews()
                        self.print_news(self.data)

                elif self.command[0] in Preset.OPEN_LINK_COMMANDS:
                    if len(self.command) < 2:
                        print("Please choose information ID.")
                    else:
                        try:
                            self.id = int(self.command[1])
                            if 0 <= self.id < 5:
                                print(f"Browser: Showing ID: {self.id}")
                                Browser(self.data[0][self.id][-1])
                            elif 5 <= self.id < 10:
                                print(f"Browser: Showing ID: {self.id}")
                                Browser(self.data[1][self.id-5][-1])
                            else:
                                print("BrowserError: Incorrect ID.")
                        except ValueError:
                            if self.command[1] in Preset.URLS.keys():
                                print(f"Opening {self.command[1]}-web.")
                                Browser(Preset.URLS[self.command[1]])
                            else:
                                print("I don't know this url.")
                else:
                    print("Sorry, I don't know this command.")
            except IndexError:
                pass

    def get_fitnews(self, starting_index=0):
        news = []

        res = requests.get(Preset.URLS["fit"])
        if res.status_code == 200:
            res = BeautifulSoup(res.content, "html.parser")
            new_msg = res.find_all(class_="b-news__title pb10", itemprop="name")
            new_msg_dates = res.find_all(class_="b-news__date font-secondary")
            msg_links = res.find_all(class_="b-news__link")

            for i in range(5):
                # No., Date, Title, Link
                news.append([i+starting_index, new_msg_dates[i].text, new_msg[i].text, new_msg[i].next_sibling])

            i = 0
            for link in msg_links[:5]:
                news[i][-1] = link['href']
                i += 1

            return news
        else:
            return f"ERROR {res.status_code} in loading FIT News\n"

    def get_vutnews(self, starting_index=5):
        news = []

        res = requests.get(Preset.URLS["vut"])
        if res.status_code == 200:
            res = BeautifulSoup(res.content, "html.parser")
            new_msg = res.find_all(class_="b-news__title h3")
            new_msg_dates = res.find_all(class_="b-news__date font-secondary")
            msg_links = res.find_all(class_="b-news__link")

            for i in range(5):
                # No., Date, Title, Link
                news.append([i+starting_index, new_msg_dates[i].text[12:-11], new_msg[i].text, new_msg[i].next_sibling])

            i = 0
            for link in msg_links[:5]:
                news[i][-1] = link['href']
                i += 1

            return news
        else:
            return f"ERROR {res.status_code} in loading VUT News\n"

    def print_news(self, data):
        if data != [[], []] or data != []:
            if len(data) > 0:
                c = 0
                for q in data:
                    if len(q) < 6:
                        # normal occasion
                        
                        if c == 1:
                            MONTHS = ['leden', 'únor', 'březen', 'duben', 'květen', 'červen', 'červenec', 'srpen', 'září',
                                      'říjen', 'listopad', 'prosinec']
                        else:
                            MONTHS = ['ledna', 'února', 'března', 'dubna', 'května', 'června', 'července', 'srpna', 'září',
                                      'října', 'listopadu', 'prosince']

                        dateTime = str(datetime.now()).split()
                        date = dateTime[0].split("-")[::-1]
                        date[1] = MONTHS[int(date[1]) - 1]
                        date[0] = str(int(date[0]))

                        print(" #ID    Date        Title")
                        print(" ------------------------")
                        for e in q:
                            msg_date = e[1].split()
                            msg_date[0] = msg_date[0][:-1]
                            if msg_date[1] == date[1] and msg_date[0] == date[0]:
                                line = f" |{e[0]}| {e[1]} | * {e[2]}"
                            else:
                                line = f" |{e[0]}| {e[1]} |   {e[2]}"

                            print(line)
                            if e[0] == 4 or e[0] == 9:
                                print(' ' + '-'*len(line))
                            else:
                                print(' ------------------------')
                    else:
                        # TODO: check if this is ERROR message
                        print(q)
                    c += 1
            else:
                print("ERROR: Data empty\n")
        else:
            print("I've got nothing for you.")
