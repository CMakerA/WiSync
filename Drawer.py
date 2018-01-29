import pygame
from Dimensions import *
from Color import *


def draw_rect(zone: Zone, color: Color, window: pygame.Surface):
    print("Drawing rect " + zone.to_string() + " with color " + color.to_string())
    pygame.draw.rect(window, color.get(), zone.get())
