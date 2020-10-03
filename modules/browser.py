import webbrowser


class Browser:
    def __init__(self, URL="https://duckduckgo.com/"):
        self.browser = webbrowser
        self.URL = URL
        try:
            self.browser.open_new(self.URL)
        except:
            print("I am having trouble with accessing this website.")
