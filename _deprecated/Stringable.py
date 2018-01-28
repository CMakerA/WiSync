import abc


class Stringable:
    def __init__(self, class_name: str):
        self.class_name = class_name

    def parse_to_string(self, values: list()):
        to_return = ""
        for value in values:
            if to_return is "":
                to_return += str(value)
            else:
                to_return += ", " + str(value)
        return self.class_name + "(" + to_return + ")"

    @abc.abstractmethod
    def to_string(self) -> str:
        pass
