class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(other.x - self.x, other.y - self.y)

    def get(self) -> (int, int):
        return self.x, self.y

    def to_string(self) -> str:
        return "Vector2(" + str(self.x) + ", " + str(self.y) + ")"


blankVector2 = Vector2(0, 0)


class ArrayPosition(Vector2):
    def __init__(self, value: (int, int)):
        super().__init__(value[0], value[1])


class Zone:
    def __init__(self, vector1: Vector2, vector2: Vector2):
        self.vector1 = vector1
        self.vector2 = vector2

    def point_over(self, point: Vector2):
        return self.vector1.x < point.x < self.vector2.x and self.vector1.y < point.y < self.vector2.y

    def get_vectors(self) -> (Vector2, Vector2):
        return self.vector1, self.vector2

    def get(self) -> (int, int, int, int):
        return self.vector1.x, self.vector1.y, self.vector2.x, self.vector2.y

    def to_string(self) -> str:
        return "Zone(" + str(self.vector1.x) + ", " + str(self.vector1.y) + ", " + str(self.vector2.x) + ", " + str(
            self.vector2.y) + ")"


class Position(Vector2):
    def to_string(self) -> str:
        return "Position(" + str(self.x) + ", " + str(self.y) + ")"


class Size(Vector2):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

        self.width = width
        self.height = height

    def to_string(self) -> str:
        return "Size(" + str(self.x) + ", " + str(self.y) + ")"
