from Dimensions import *
from Color import *
from Ider import *
import Drawer
import Printer
import pygame
import pygame.image
from pygame.locals import *
from enum import Enum
import os


class UIElement:
    window = None

    multiple_click_wait_time = 300

    def __init__(self, size: Size, position: Position, background_color: Color, click_background_color: Color,
                 hover_background_color: Color):
        self.size = size
        self.position = position
        self.zone = Zone(position, Vector2(position.x + size.x, position.y + size.y))

        self.background_color = background_color
        self.click_background_color = click_background_color
        self.hover_background_color = hover_background_color
        self.current_color = self.background_color

        self.id = Iders.btnIder.add(self)

    __clicked = False

    def draw(self):
        mousepos = ArrayPosition(pygame.mouse.get_pos())
        if self.zone.point_over(mousepos):
            if pygame.mouse.get_pressed()[0]:
                self.current_color = self.click_background_color
                if not self.__clicked:
                    self.__clicked = True
                    print("Click!")
            else:
                self.__clicked = False
                self.current_color = self.hover_background_color
        else:
            self.current_color = self.background_color

        Printer.print_once("Initialized " + self.id + " in " + self.position.to_string() + " with size " +
                           self.size.to_string() + ". " + self.zone.to_string())
        if self.window is not None:
            # pygame.draw.rect(self.window, self.current_color.get(), self.zone.get())
            Drawer.draw_rect(self.zone, self.current_color, self.window)
        else:
            Printer.print_once(self.id + " has not a window to be on.")


class UIThemes(Enum):
    normal = 0
    light = 1
    dark = 2


class Button(UIElement):
    __background_colors = [Colors.flat_salmon_red, Colors.flat_light_sea_blue, Colors.flat_brown]

    def __init__(self, size: Size, position: Position, theme: UIThemes):
        self.size = size
        self.position = position

        # TODO: Click and hover colors
        super().__init__(self.size, self.position, self.__background_colors[theme.value], Colors.flat_light_sea_blue,
                         Colors.flat_pink)


class Window:
    running = False

    def __init__(self, size: Size, title: str, icon_file_name: str = None,
                 background_color: Color = Colors.flat_dark_gray):
        self.size = size
        self.title = title
        self.background_color = background_color

        if icon_file_name is not None:
            a = pygame.image.load(os.path.join(icon_file_name))
            pygame.display.set_icon(a)

        self.elements = list()

        self.screen = pygame.display.set_mode((self.size.width, self.size.height))
        pygame.display.set_caption(self.title)
        self.screen.fill(self.background_color.get())

    def add(self, element: UIElement):
        self.elements.append(element)

    def __main_loop(self):
        while self.running:
            # Draw all the elements
            for element in self.elements:
                element.draw()

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    self.running = False

    def start(self):
        self.running = True
        for element in self.elements:
            element.window = self.screen
        pygame.display.flip()
        self.__main_loop()
