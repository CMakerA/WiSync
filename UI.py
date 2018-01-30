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
import os


class UIElement:
    window = None

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

    __clicked = False
    __hovered = False
    __left = True

    new_pos = None

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
            if self.zone.point_over(mousepos):
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


class Label(UIElement):
    def __init__(self, position: Position, text: str, text_color: Color = Colors.black, font: Font = Fonts.comic_sans):
        self.position = position
        self.text = text
        self.color = text_color
        self.font = font

        super().__init__("lbl", blankVector2, self.position, Colors.transparent, Colors.transparent, Colors.transparent)

    def draw(self, start_position: Vector2 = None):
        Drawer.draw_text(self.position, self.color, self.text, self.font, self.window)


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


class TextBox(UIElement):
    __blink_time = 500  # In millis

    def __init__(self, size: Size, position: Position, text: str, font: Font = Font(Fonts.comic_sans.name, 15)):
        self.position = position
        self.size = size
        self.text = text
        self.font = font

        self.elements = list()

        super().__init__("txt", self.size, self.position)

        self.style = Styles.text_box

        self.__last_blink_time = Time.millis()

    def add(self, element: UIElement):
        self.elements.append(element)

    focused = False

    __last_blink_shown = False

    def draw(self, start_position: Vector2 = None):
        Printer.print_once("Initialized " + self.id + " in " + self.position.to_string() + " with size " +
                           self.size.to_string() + ". " + self.zone.to_string())

        if pygame.mouse.get_pressed()[0]:
            if self.zone.point_over(Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
                self.focused = True
                print("Focused!")
            else:
                self.focused = False
                print("Unfocused!")

        if self.focused:
            # Drawer.draw_border_rect(self.zone, self.style.focused_background_color, BorderStyle(
            #     self.style.focused_border_color, self.style.border_width), self.window)
            Drawer.draw_rounded_border_rect(self.zone, self.style.focused_background_color, BorderStyle(
                self.style.border_color, self.style.border_width), self.window)

            if Time.millis() - self.__last_blink_shown > self.__blink_time:
                if self.__last_blink_shown:
                    # draw down line
                    pass
                else:
                    # don't draw line
                    pass
                self.__last_blink_shown = not self.__last_blink_shown

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.text += " "
                    elif event.key == pygame.K_BACKSLASH:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    print(self.id + " text is \"" + self.text + "\"")

            Drawer.draw_text(self.zone.vector1 + Vector2(5, 5), Colors.black, self.text, self.font, self.window)
        else:
            # Drawer.draw_border_rect(self.zone, self.style.background_color, BorderStyle(
            #     self.style.border_color, self.style.border_width), self.window)
            Drawer.draw_rounded_border_rect(self.zone, self.style.background_color, BorderStyle(
                self.style.border_color, self.style.border_width), self.window)


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
