import pygame
from _deprecated import Font
from _deprecated.style.Style import *
from _deprecated.Dimensions import *
from _deprecated.Printer import *


class Drawer:
    @staticmethod
    def draw_rect(zone: Zone, color: Color, display: pygame.Surface):
        pygame.draw.rect(display, color.get(), zone.get())

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
        self.printer = Printer()

    def draw(self, starting_point: Vector2 = None):
        if self.window is not None:
            if self.size is not None:
                if starting_point is None:
                    Drawer.draw_rect(Zone(self.position, self.size), self.style.background_color, self.window)
                else:
                    Drawer.draw_rect(Zone(starting_point + self.position, self.size), self.style.background_color,
                                     self.window)

    def add_to(self, window: pygame.display):
        self.window = window


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

        self.current_zone = Zone(self.position, self.position + self.size)
        self.starting_point = None

    # <editor-fold desc="Events">
    def perform_click(self):
        if self.window is not None:
            self.currentStyle = self.click_style
            if self.on_click is not None:
                self.on_click()

    def perform_hover(self):
        if self.window is not None:
            self.currentStyle = self.hover_style
            if self.on_hover is not None:
                self.on_hover()

    def perform_leave(self):
        if self.window is not None:
            self.currentStyle = self.idle_style
            if self.on_leave is not None:
                self.on_leave()

    # </editor-fold>

    def point_over(self, point: Vector2) -> bool:
        return self.get_zone().is_in(point)

    addedPos = False

    def draw(self, starting_point: Vector2 = None):
        # if self.window is not None:
        #     if self.size is not None:
        #         Drawer.draw_rect(self.get_zone(), self.currentStyle.background_color, self.window)
        super().draw()

    def set_pos(self, new_position: Vector2):
        self.position = new_position

    def get_zone(self) -> Zone:
        if self.starting_point is None:
            return Zone(self.position, self.position + self.size)
        else:
            return Zone(self.starting_point + self.position, self.starting_point + self.position + self.size)


class Ider:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self.ids = list()

    def add(self, element) -> str:
        self.ids.append(element)
        return self.prefix + str(len(self.ids))


class Iders:
    btnIdler = Ider("btn")
    panelIder = Ider("pnl")
