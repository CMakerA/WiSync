from elements.Panel import *


class HeaderPanel(Panel):
    # left-right and top-bottom
    __header_margins = Vector2(30, 20)

    panel_style = Style(Colors.background_gray, Colors.white, Colors.transparent, 0, 0)
    header_style = Style(Colors.salmon_red, Colors.white, Colors.transparent, 0, 0)

    def __init__(self, position: Vector2, size: Vector2, header_text: str):
        super().__init__(position, size, self.panel_style)

        self.header_size = Vector2(size.x, 23)

        self.header_style = self.header_style
        self.header_text = header_text
        self.text = Font.create_text(header_text, self.font_preferences, 20,
                                     self.header_style.text_color.get_no_alpha())

        self.midpoint = size.x / 2

    def draw(self, starting_point: Vector2 = None):
        if self.window is not None:
            Drawer.draw_rect(self.position + Vector2(0, self.header_size.y), self.size,
                             self.panel_style.background_color, self.window)
            Drawer.draw_rect(self.position, self.header_size, self.header_style.background_color, self.window)
            Drawer.draw_text(
                self.position + Vector2(int(3 * (self.__header_margins.x / 4)), int(3 * (self.__header_margins.y / 4))),
                self.text,
                self.window)
        for element in self.elements:
            element.window = self.window
            element.draw(self.position + Vector2(0, self.header_size.y))
