from Dimensions import *
from Color import *
from Font import *
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
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            if pygame.mouse.get_pressed()[0]:
                self.current_color = self.click_background_color
                if not self.__clicked:
                    self.__clicked = True
                    print("Click!")
            else:
                self.__clicked = False
                self.current_color = self.hover_background_color
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            self.current_color = self.background_color

        Printer.print_once("Initialized " + self.id + " in " + self.position.to_string() + " with size " +
                           self.size.to_string() + ". " + self.zone.to_string())
        if self.window is not None:
            # TODO: Make drawing work
            # pygame.draw.rect(self.window, self.current_color.get(), self.zone.get())
            Drawer.draw_rect(self.zone, self.current_color, self.window)
        else:
            Printer.print_once(self.id + " has not a window to be on.")


class Label(UIElement):
    def __init__(self, position: Position, text: str, text_color: Color = Colors.black, font: Font = Fonts.comic_sans):
        self.position = position
        self.text = text
        self.color = text_color
        self.font = font

        super().__init__(blankVector2, self.position, Colors.transparent, Colors.transparent, Colors.transparent)

    def draw(self):
        Drawer.draw_text(self.position, self.color, self.text, self.font, self.window)


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

        super().__init__(self.size, self.position, self.__background_colors[theme.value],
                         self.__click_background_colors[theme.value],
                         self.__hover_background_colors[theme.value])

    def draw(self):
        super().draw()

        Drawer.draw_text(self.position + Vector2(5, 5), Colors.black, self.text, self.font, self.window)


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

        pygame.font.init()
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

            pygame.display.update()

    def start(self):
        self.running = True
        for element in self.elements:
            element.window = self.screen
        pygame.display.flip()
        self.__main_loop()
