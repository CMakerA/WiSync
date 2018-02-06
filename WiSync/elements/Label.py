from Dimensions import *
from Style import *
from Font import *
from Ider import *
import Drawer
from pygame.locals import *
from elements.UIElement import *


class Label(UIElement):
    def __init__(self, position: Position, text: str, text_color: Color = Colors.black, font: Font = Fonts.comic_sans):
        self.position = position
        self.text = text
        self.color = text_color
        self.font = font

        super().__init__("lbl", blankVector2, self.position, Colors.transparent, Colors.transparent, Colors.transparent)

    def draw(self, start_position: Vector2 = None):
        Drawer.draw_text(self.position, self.color, self.text, self.font, self.window)