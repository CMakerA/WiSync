import sys
from UIElement import *


class Window:
    running = True

    elements = []

    def __init__(self, size: Vector2, title: str, background: Color):
        pygame.display.init()
        self.screen = pygame.display.set_mode([size.x, size.y])
        pygame.display.set_caption(title)
        self.screen.fill(background.get())

    def add(self, element: UIElement):
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
