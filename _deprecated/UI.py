import sys


class Window:
    running = True

    elements = []

    def __init__(self, size: Vector2, title: str, background: Color):
        pygame.init()
        if size.x is 0 and size.y is 0:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            pygame.display.set_caption(title)

            info_object = pygame.display.Info()

            size = Vector2(info_object.current_w, info_object.current_h)

            window_zone = Zone(Vector2(0, 0), size)
        else:
            self.screen = pygame.display.set_mode([size.x, size.y])
            pygame.display.set_caption(title)

            window_zone = Zone(Vector2(0, 0), size)

        pygame.draw.rect(self.screen, background.get(), window_zone.get())

    def add(self, element: UIElement):
        element.add_to(self.screen)
        self.elements.append(element)

    def __start_ticking(self):
        while self.running:
            mouse_pos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            for element in self.elements:
                if element.window is not None:
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
                    else:
                        element.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                            pygame.quit()
                            sys.exit()
            pygame.display.update()

    def start(self):
        pygame.display.flip()

        self.__start_ticking()
