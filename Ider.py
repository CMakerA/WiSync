class Ider:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self.elements = list()

    def __len__(self) -> int:
        return len(self.elements)

    def add(self, element) -> str:
        self.elements.append(element)
        return self.prefix + str(len(self))


class Iders:
    btnIder = Ider("btn")
