from Dimensions import *
from Color import *
from Font import *


def draw_rect(zone: Zone, color: Color, window: pygame.Surface):
    pygame.draw.rect(window, color.get(), zone.get())


def draw_text(position: Vector2, color: Color, text: str, font: Font, window: pygame.Surface):
    textsurface = font.get().render(text, False, color.get())
    window.blit(textsurface, position.get())
