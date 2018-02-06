from Dimensions import *
from Style import *
from Font import *
from Ider import *
import Drawer
import Printer
import pygame
import pygame.image
from pygame.locals import *

class UIElement:
    window = None
    window_class = None

    def __init__(self, prefix: str, size: Size, position: Position, background_color: Color = Colors.white,
                 click_background_color: Color = Colors.white,
                 hover_background_color: Color = Colors.white,
                 style: Style = None):
        self.size = size
        self.position = position
        self.__update_zone()

        self.background_color = background_color
        self.click_background_color = click_background_color
        self.hover_background_color = hover_background_color
        self.current_color = self.background_color
        self.style = style

        self.on_click = None
        self.on_hover = None
        self.on_leave = None

        ider = iders.ider_from_str(prefix)
        self.id = ider.add(self)

        self.event_handler = None

    __clicked = False
    __hovered = False
    __left = True

    new_pos = None

    def has_event_handler(self) -> bool:
        return self.event_handler is not None

    def __update_zone(self, position: Position = None):
        if position is None:
            # self.zone = Zone(self.position, Vector2(self.position.x + self.size.x, self.position.y + self.size.y))
            self.zone = Zone(self.position, self.size)
        else:
            # self.zone = Zone(position, Vector2(self.position.x + self.size.x, self.position.y + self.size.y))
            self.zone = Zone(position, self.size)

    def draw(self, start_position: Vector2 = None):
        if self.window is not None:
            if start_position is not None:
                self.new_pos = start_position + self.position
                self.__update_zone(self.new_pos)

            mousepos = ArrayPosition(pygame.mouse.get_pos())
            hitbox = Zone.zone_correction(self.zone)
            if hitbox.point_over(mousepos):
                self.__left = False
                if pygame.mouse.get_pressed()[0]:
                    self.current_color = self.click_background_color
                    if not self.__clicked:
                        self.__clicked = True
                        if self.on_click is not None:
                            self.on_click()
                else:
                    self.__clicked = False
                    self.current_color = self.hover_background_color
                    if not self.__hovered:
                        self.__hovered = True
                        if self.on_hover is not None:
                            self.on_hover()
            else:
                self.__hovered = False
                self.current_color = self.background_color
                if not self.__left:
                    self.__left = True
                    if self.on_leave is not None:
                        self.on_leave()

            Printer.print_once("Initialized " + self.id + " in " + self.position.to_string() + " with size " +
                               self.size.to_string() + ". " + self.zone.to_string())

            Drawer.draw_rect(self.zone, self.current_color, self.window)
        else:
            Printer.print_once(self.id + " has not a window to be on.")