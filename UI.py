import pygame
import sys
import Font
from Color import *


# <editor-fold desc="UI Helpers">
# <editor-fold desc="Dimensions">
class Vector2:
    def __init__(self, x: int, y: int = None):
        if y is not None:
            self.x = x
            self.y = y
        else:
            self.x = x
            self.y = x

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def get(self) -> (int, int):
        return self.x, self.y


class Zone:
    def __init__(self, vector1: Vector2, vector2: Vector2):
        self.vector1 = vector1
        self.vector2 = vector2

    def is_in(self, point: Vector2) -> bool:
        return self.vector1.x < point.x < self.vector2.x and self.vector1.y < point.y < self.vector2.y


# </editor-fold>

class Ider:
    def __init__(self):
        self.ids = list()

    def add(self, element) -> str:
        self.ids.append(element)
        return "btn" + str(len(self.ids))


# <editor-fold desc="Colors">
class Colors:
    blue = Color(0, 0, 255)
    shadow = Color(120, 120, 120, 25)
    white = Color(255, 255, 255)
    black = Color(0, 0, 0)
    transparent = Color(0, 0, 0, 0)
    red = Color(255, 0, 0)
    yellow = Color(255, 255, 0)
    aqua_blue = rgba(85, 239, 196, 1.0)
    salmon_red = rgba(255, 118, 117, 1.0)
    background_gray = rgba(223, 230, 233, 1.0)


class Style:
    def __init__(self, background_color: Color, text_color: Color, border_color: Color, border_width: int,
                 border_radius: int):
        self.background_color = background_color

        self.text_color = text_color

        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius


# </editor-fold>

class Drawer:
    @staticmethod
    def draw_rect(position: Vector2, size: Vector2, color: Color, display: pygame.Surface):
        pygame.draw.rect(display, color.get(), (position.x, position.y, position.x + size.x, position.y + size.y))

    @staticmethod
    def draw_text(position: Vector2, text: Font, display: pygame.Surface):
        display.blit(text, position.get())


# </editor-fold>

# <editor-fold desc="UI Elements">
class UIElement:
    window = None

    font_preferences = Font.futura_TEE_preferences

    def __init__(self, position: Vector2, size: Vector2, style: Style):
        self.position = position
        self.size = size
        self.style = style

    def draw(self):
        if self.window is not None:
            Drawer.draw_rect(self.position, self.size, self.style.background_color, self.window)


class InteractableUIElement(UIElement):
    window = None

    justHovered = False
    justClicked = False

    def __init__(self, position: Vector2, idle_style: Style, hover_style: Style, click_style: Style,
                 size: Vector2 = None,
                 on_click=None, on_hover=None, on_leave=None):
        super().__init__(position, size, idle_style)

        self.idle_style = idle_style
        self.hover_style = hover_style
        self.click_style = click_style

        self.currentStyle = idle_style

        self.on_click = on_click
        self.on_hover = on_hover
        self.on_leave = on_leave

    def perform_click(self):
        self.currentStyle = self.click_style
        if self.on_click is not None:
            self.on_click()

    def perform_hover(self):
        self.currentStyle = self.hover_style
        if self.on_hover is not None:
            self.on_hover()

    def perform_leave(self):
        self.currentStyle = self.idle_style
        if self.on_leave is not None:
            self.on_leave()

    def point_over(self, point: Vector2) -> bool:
        return self.get_zone().is_in(point)

    def draw(self):
        if self.window is not None:
            if self.size is not None:
                Drawer.draw_rect(self.position, self.size, self.currentStyle.background_color, self.window)

    def get_zone(self):
        return Zone(self.position, self.position + self.size)


class Iders:
    btnIdler = Ider()
    panelIder = Ider()


class Panel(UIElement):
    def __init__(self, position: Vector2, size: Vector2, style: Style):
        super().__init__(position, size, style)

        self.id = Iders.panelIder.add(self)


class HeaderPanel(Panel):
    # left-right and top-bottom
    __header_margins = Vector2(30, 20)

    panel_style = Style(Colors.background_gray, Colors.white, Colors.transparent, 0, 0)
    header_style = Style(Colors.salmon_red, Colors.white, Colors.transparent, 0, 0)

    def __init__(self, position: Vector2, size: Vector2, header_text: str):
        super().__init__(position, size, self.panel_style)

        self.header_style = self.header_style
        self.header_text = header_text
        self.text = Font.create_text(header_text, self.font_preferences, 20, self.header_style.background_color.get())

    def draw(self):
        if self.window is not None:
            height = len(self.header_text) + self.__header_margins.y
            width = len(self.header_text) + self.__header_margins.x
            Drawer.draw_rect(self.position, Vector2(width, height), self.style.background_color, self.window)


class Button(InteractableUIElement):
    __idle = Style(Color(255, 118, 117), Colors.transparent, Colors.transparent, 0, 30)
    __hover = Style(Colors.red, Colors.transparent, Colors.transparent, 0, 30)
    __click = Style(Colors.yellow, Colors.transparent, Colors.transparent, 0, 30)

    __font_margin = 15

    def __init__(self, btn_text: str, position: Vector2, size: Vector2 = None, on_click=None, on_hover=None,
                 on_leave=None):
        text = Font.create_text(btn_text, self.font_preferences, 20, Colors.white.get())
        super().__init__(size, self.__idle, self.__hover, self.__click, position, on_click, on_hover, on_leave)

        if size is None:
            self.size = Vector2(self.text.size + (self.__font_margin * 2),
                                (self.text.size * len(text)) + (self.__font_margin * 2))

        self.text = text

        self.id = Iders.btnIdler.add(self)

        print("Initialized Button with id " + self.id + ", in coordinates (" + str(position.x) + ", " + str(
            position.y) + "), with size(" + str(size.x) + ", " + str(size.y) + ")")

    def get_window(self):
        return self.window

    def draw(self):
        super().draw()
        Drawer.draw_text(self.position + Vector2(int(self.__font_margin - (20 / 100 * self.__font_margin))), self.text,
                         self.window)


class Window:
    running = True

    elements = []

    def __init__(self, size: Vector2, title: str, background: Color):
        pygame.display.init()
        self.screen = pygame.display.set_mode([size.x, size.y])
        pygame.display.set_caption(title)
        self.screen.fill(background.get())

    def add(self, element: InteractableUIElement):
        element.window = self.screen
        self.elements.append(element)

    def __start_ticking(self):
        while self.running:
            mouse_pos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            for element in self.elements:
                if isinstance(element, InteractableUIElement):
                    if element.point_over(mouse_pos):
                        if pygame.mouse.get_pressed()[0]:
                            if not element.justClicked:
                                element.justClicked = True
                                element.perform_click()
                        else:
                            element.justClicked = False
                            element.perform_hover()
                            element.justHovered = True
                    else:
                        element.justClicked = False
                        if element.justHovered:
                            element.justHovered = False
                            element.perform_leave()

            for element in self.elements:
                element.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def start(self):
        pygame.display.flip()

        self.__start_ticking()

# </editor-fold>
