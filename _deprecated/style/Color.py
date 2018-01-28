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

    def get_no_alpha(self) -> (int, int, int):
        return self.red, self.green, self.blue

    def get_force_alpha(self) -> (int, int, int, int):
        return self.red, self.green, self.blue, 0


class rgb(Color):
    def __init__(self, r: int, g: int, b: int):
        super().__init__(r, g, b)


class rgba(Color):
    # The input alpha is a  value between 0 and 1
    def __init__(self, r: int, g: int, b: int, a: float):
        super().__init__(r, g, b, int(255 * a))


class Colors:
    blue = Color(0, 0, 255)
    shadow = Color(120, 120, 120, 25)
    white = Color(255, 255, 255)
    black = Color(0, 0, 0)
    transparent = Color(0, 0, 0, 0)
    red = Color(255, 0, 0)
    yellow = Color(255, 255, 0)
    aqua_blue = rgba(85, 239, 196, 1.0)
    flat_pink = rgba(255, 118, 117, 1.0)
    background_gray = rgba(223, 230, 233, 1.0)
    dark_gray = rgba(45, 52, 54, 1.0)
    electric_blue = rgba(9, 132, 227, 1.0)
    light_pink = rgba(253, 121, 168, 1.0)
