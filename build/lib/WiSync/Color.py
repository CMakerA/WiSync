class Color:
    def __init__(self, r: int, g: int, b: int, a_float: float = -1.0, a_int: int = 255):
        self.r = r
        self.g = g
        self.b = b
        if a_float >= 0:
            self.a = a_float * 255
        else:
            self.a = a_int
        self.name = None

    def get(self) -> (int, int, int, int):
        return self.r, self.g, self.b, self.a

    def with_name(self, name: str):
        self.name = name

        return self

    def to_string(self) -> str:
        if self.name is None:
            return str(self.get())
        else:
            return self.name


class rgba(Color):
    pass


class Colors:
    transparent = Color(255, 255, 255).with_name("transparent")

    black = Color(0, 0, 0).with_name("black")
    white = Color(255, 255, 255).with_name("white")
    red = Color(255, 0, 0).with_name("red")
    green = Color(0, 255, 0).with_name("green")
    blue = Color(0, 0, 255).with_name("blue")

    # American flat color palette
    flat_light_aqua = rgba(85, 239, 196, 1.0).with_name("flat_light_aqua")
    flat_light_sea_blue = rgba(129, 236, 236, 1.0).with_name("flat_light_sea_blue")
    flat_light_blue = rgba(116, 185, 255, 1.0).with_name("flat_light_blue")
    flat_light_purple = rgba(162, 155, 254, 1.0).with_name("flat_light_purple")
    flat_light_white_gray = rgba(223, 230, 233, 1.0).with_name("flat_light_white_gray")
    flat_dark_aqua = rgba(0, 184, 148, 1.0).with_name("flat_dark_aqua")
    flat_aqua = rgba(0, 206, 201, 1.0).with_name("flat_aqua")
    flat_blue = rgba(9, 132, 227, 1.0).with_name("flat_blue")
    flat_purple = rgba(108, 92, 231, 1.0).with_name("flat_purple")
    flat_light_gray = rgba(178, 190, 195, 1.0).with_name("flat_light_gray")
    flat_cream = rgba(255, 234, 167, 1.0).with_name("flat_cream")
    flat_light_salmon = rgba(250, 177, 160, 1.0).with_name("flat_light_salmon")
    flat_salmon_red = rgba(255, 118, 117, 1.0).with_name("flat_salmon_red")
    flat_light_pink = rgba(253, 121, 168, 1.0).with_name("flat_light_pink")
    flat_gray = rgba(99, 110, 114, 1.0).with_name("flat_gray")
    flat_cream_yellow = rgba(253, 203, 110, 1.0).with_name("flat_cream_yellow")
    flat_brown = rgba(225, 112, 85, 1.0).with_name("flat_brown")
    flat_red = rgba(214, 48, 49, 1.0).with_name("flat_red")
    flat_pink = rgba(232, 67, 147, 1.0).with_name("flat_pink")
    flat_dark_gray = rgba(45, 52, 54, 1.0).with_name("flat_dark_gray")
