class Printer:
    def __init__(self):
        self.printed_cache = []

    def print_once(self, text: str):
        if text not in self.printed_cache:
            print(text)
            self.printed_cache.append(text)
