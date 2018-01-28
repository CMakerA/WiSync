from style.Color import *


class Style:
    def __init__(self, background_color: Color, text_color: Color, border_color: Color, border_width: int,
                 border_radius: int):
        self.background_color = background_color

        self.text_color = text_color

        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius


class Styles:
    blue_button = Style(Colors.electric_blue, Colors.white, Colors.transparent, 0, 30)
    red_button = Style(Color(255, 118, 117), Colors.white, Colors.transparent, 0, 30)
    gray_panel = Style(Colors.background_gray, Colors.transparent, Colors.transparent, 0, 30)
