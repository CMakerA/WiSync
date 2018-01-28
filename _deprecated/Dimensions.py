from _deprecated.Stringable import *


class Vector2(Stringable):
    def __init__(self, x: int, y: int = None):
        super().__init__("Vector2")
        if y is not None:
            self.x = x
            self.y = y
        else:
            self.x = x
            self.y = x

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def get(self) -> (int, int):
        return self.x, self.y

    def to_string(self) -> str:
        return super().parse_to_string([self.x, self.y])


class Position(Vector2):
    pass


class Size(Vector2):
    pass


class Zone(Stringable):
    def __init__(self, vector1: Vector2, vector2: Vector2):
        super().__init__("Zone")
        self.vector1 = vector1
        self.vector2 = vector2

    def is_in(self, point: Vector2) -> bool:
        return self.vector1.x < point.x < self.vector2.x and self.vector1.y < point.y < self.vector2.y

    def get(self) -> (int, int, int, int):
        return self.vector1.x, self.vector1.y, self.vector2.x, self.vector2.y

    def to_string(self) -> str:
        return super().parse_to_string([self.vector1.x, self.vector1.y, self.vector2.x, self.vector2.y])
