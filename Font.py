import pygame


class Font:
    def __init__(self, family: str, size: int):
        pygame.font.init()
        self.name = family
        self.font = pygame.font.SysFont(self.name, size)

    def get(self) -> pygame.font:
        return self.font


class Fonts:
    comic_sans = Font('Comic Sans MS', 30)
