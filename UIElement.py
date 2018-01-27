import pygame
import Font
from style.Style import *
from Dimensions import *


class Drawer:
    @staticmethod
    def draw_rect(position: Vector2, size: Vector2, color: Color, display: pygame.Surface):
        pygame.draw.rect(display, color.get(), (position.x, position.y, position.x + size.x, position.y + size.y))

    @staticmethod
    def draw_text(position: Vector2, text: Font, display: pygame.Surface):
        display.blit(text, position.get())


class UIElement:
    window = None

    font_preferences = Font.futura_TEE_preferences

    def __init__(self, position: Vector2, size: Vector2, style: Style):
        self.position = position
        self.size = size
        self.style = style

    def draw(self, starting_point: Vector2 = None):
        if self.window is not None:
            if self.size is not None:
                if starting_point is None:
                    Drawer.draw_rect(self.position, self.size, self.style.background_color, self.window)
                else:
                    Drawer.draw_rect(starting_point + self.position, self.size, self.style.background_color,
                                     self.window)


class InteractableUIElement(UIElement):
    window = None

    justHovered = False
    justClicked = False

    def __init__(self, position: Vector2, idle_style: Style, hover_style: Style, click_style: Style,
                 size: Vector2 = None, on_click=None, on_hover=None, on_leave=None):
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

    addedPos = False

    def draw(self, starting_point: Vector2 = None):
        if self.window is not None:
            if self.size is not None:
                Drawer.draw_rect(self.position, self.size, self.currentStyle.background_color, self.window)

    def set_pos(self, new_position: Vector2):
        self.position = new_position

    def get_zone(self):
        return Zone(self.position, self.position + self.size)


class Ider:
    def __init__(self):
        self.ids = list()

    def add(self, element) -> str:
        self.ids.append(element)
        return "btn" + str(len(self.ids))


class Iders:
    btnIdler = Ider()
    panelIder = Ider()
