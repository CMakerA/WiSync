from Dimensions import *
from Style import *
from Font import *
from Ider import *
import Drawer
from enum import Enum
from elements.UIElement import *


class UIThemes(Enum):
    normal = 0
    light = 1
    dark = 2


class Button(UIElement):
    __background_colors = [Colors.flat_salmon_red, Colors.flat_light_blue, Colors.flat_brown]
    __hover_background_colors = [Colors.flat_brown, Colors.flat_light_blue, Colors.flat_red]
    __click_background_colors = [Colors.flat_salmon_red, Colors.flat_blue, Colors.flat_brown]

    def __init__(self, size: Size, position: Position, text: str, theme: UIThemes,
                 font: Font = Font(Fonts.comic_sans.name, 15)):
        self.size = size
        self.position = position
        self.theme = theme
        self.text = text
        self.font = font

        super().__init__("btn", self.size, self.position, self.__background_colors[theme.value],
                         self.__click_background_colors[theme.value],
                         self.__hover_background_colors[theme.value])

    def draw(self, start_position: Vector2 = None):
        super().draw(start_position)

        Drawer.draw_text(self.zone.vector1 + Vector2(5, 5), Colors.black, self.text, self.font, self.window)