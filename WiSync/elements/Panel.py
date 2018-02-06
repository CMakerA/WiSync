from Dimensions import *
from Style import *
from Font import *
from Ider import *
import Drawer
from pygame.locals import *
from elements.UIElement import *


class Panel(UIElement):
    def __init__(self, position: Position, size: Size, background_color: Color):
        self.position = position
        self.size = size

        self.elements = list()

        super().__init__("pnl", self.size, self.position, background_color, background_color, background_color)

    def add(self, element: UIElement):
        self.elements.append(element)

    def draw(self, start_position: Vector2 = None):
        super().draw(start_position)
        for element in self.elements:
            element.window = self.window
            element.draw(self.position)