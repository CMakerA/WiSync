import pygame
from Dimensions import *
from Color import *


def draw_rect(zone: Zone, color: Color, window: pygame.Surface):
    pygame.draw.rect(window, color.get(), zone.get())
