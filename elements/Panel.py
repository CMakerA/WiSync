from UIElement import *


class Panel(UIElement):
    elements = []

    def __init__(self, position: Vector2, size: Vector2, style: Style):
        super().__init__(position, size, style)

        self.id = Iders.panelIder.add(self)

    def add(self, element: UIElement):
        if isinstance(element, InteractableUIElement):
            element.set_pos(element.position + self.position)
        self.elements.append(element)

    def draw(self, starting_point: Vector2 = None):
        super().draw()
        for element in self.elements:
            element.draw(self.position)