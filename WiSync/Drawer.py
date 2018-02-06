from Dimensions import *
from Style import *
from Font import *
import math


def draw_rect(zone: Zone, color: Color, window: pygame.Surface):
    pygame.draw.rect(window, color.get(), zone.get())


def draw_rounded_rect(zone: Zone, color: Color, window: pygame.Surface, radius: float = 0.4):
    """
    draw_rounded_rect(window,zone,color,radius=0.4)

    zone    : rectangle
    color   : background color
    window  : destination
    radius  : 0 <= radius <= 1
    """

    rect = pygame.Rect(zone.get())
    alpha = color.a
    color.a = 0
    pos = rect.topleft
    rect.topleft = 0, 0
    rectangle = pygame.Surface(rect.size, pygame.SRCALPHA)

    circle = pygame.Surface([min(rect.size) * 3] * 2, pygame.SRCALPHA)
    pygame.draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
    circle = pygame.transform.smoothscale(circle, [int(min(rect.size) * radius)] * 2)

    radius = rectangle.blit(circle, (0, 0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle, radius)
    radius.topright = rect.topright
    rectangle.blit(circle, radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle, radius)

    rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
    rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

    rectangle.fill(color.get(), special_flags=pygame.BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MIN)

    return window.blit(rectangle, pos)


def draw_border_rect(zone: Zone, color: Color, border: BorderStyle, window: pygame.Surface):
    draw_rect(
        Zone(Vector2(zone.vector1.x - border.width, zone.vector1.y - border.width),
             Vector2(zone.vector2.x + (border.width * 2), zone.vector2.y + (border.width * 2))),
        border.color, window)
    draw_rect(zone, color, window)


def draw_rounded_border_rect(zone: Zone, color: Color, border: BorderStyle, window: pygame.Surface, radius: float = 0.4):
    draw_rounded_rect(
        Zone(Vector2(zone.vector1.x - border.width, zone.vector1.y - border.width),
             Vector2(zone.vector2.x + (border.width*2), zone.vector2.y + (border.width*2))),
        border.color, window, radius)
    draw_rounded_rect(zone, color, window, radius)


def draw_text(position: Vector2, color: Color, text: str, font: Font, window: pygame.Surface):
    textsurface = font.get().render(text, False, color.get())
    window.blit(textsurface, position.get())


def draw_line(position: Vector2, angle: int, line_length: int, line_width: float, color: Color, window: pygame.Surface):
    end_pos = Vector2(position.x + line_length*math.cos(angle), position.y + line_length*math.sin(angle))
    pygame.draw.line(window, color.get(), position.get(), end_pos.get(), line_width)
