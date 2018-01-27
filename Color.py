class Color:
    def __init__(self, red: int, green: int, blue: int, alpha: int = -1):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def has_alpha(self) -> bool:
        return self.alpha >= 0

    def get(self) -> (int, int, int, int):
        if self.has_alpha():
            return self.red, self.green, self.blue, self.alpha
        else:
            return self.red, self.green, self.blue


class rgb(Color):
    def __init__(self, r: int, g: int, b: int):
        super().__init__(r, g, b)


class rgba(Color):
    # The input alpha is a  value between 0 and 1
    def __init__(self, r: int, g: int, b: int, a: float):
        super().__init__(r, g, b, int(255*a))
