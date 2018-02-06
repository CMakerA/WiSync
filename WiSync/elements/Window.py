from Dimensions import *
from Style import *
from Font import *
from Ider import *
import Time
import Drawer
import Printer
import pygame
import pygame.image
from pygame.locals import *
from enum import Enum
import Cursors
import os
from elements.UIElement import *
from elements.TextBox import *

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

        self.draw_again()

    def draw_again(self):
        self.screen.fill(self.background_color.get())
        if self.elements is not None:
            # Draw all the elements
            for element in self.elements:
                print("Redrawing " + element.id)
                if isinstance(element, TextBox):
                    element.draw()

    def add(self, element: UIElement):
        self.elements.append(element)

    def __main_loop(self):
        while self.running:
            for event in pygame.event.get():
                for element in self.elements:
                    if element.has_event_handler():
                        element.event_handler(event)
                if event.type is pygame.QUIT:
                    self.running = False

            # Draw all the elements
            for element in self.elements:
                element.draw()

            pygame.display.update()

    def start(self):
        self.running = True
        for element in self.elements:
            element.window = self.screen
            element.window_class = self
        pygame.display.flip()
        self.__main_loop()
