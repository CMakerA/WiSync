from _deprecated.elements.Panel import *


class HeaderPanel(Panel):
    # left-right and top-bottom
    __header_margins = Vector2(30, 20)

    panel_style = Styles.gray_panel
    header_style = Style(Colors.flat_pink, Colors.white, Colors.transparent, 0, 0)

    def __init__(self, position: Vector2, size: Vector2, header_text: str):
        super().__init__(position, size)

        self.header_size = Vector2(size.x, 23)

        self.header_style = self.header_style
        self.header_text = header_text
        self.text = Font.create_text(self.header_text, self.font_preferences, 20,
                                     self.header_style.text_color.get_no_alpha())

        self.midpoint = size.x / 2

    def draw(self, starting_point: Vector2 = None):
        if self.window is not None:
            # Draw panel background
            panel_position = self.position + Vector2(0, self.header_size.y * 2)
            panel_content = Zone(panel_position, self.size)
            Drawer.draw_rect(panel_content, self.panel_style.background_color, self.window)
            # Draw all content elements
            for element in self.elements:
                element.window = self.window
                element.draw()
            # Draw panel header
            header_zone = Zone(self.position, self.header_size + Vector2(0, self.header_size.y))
            Drawer.draw_rect(header_zone, self.header_style.background_color, self.window)
            # Write panel header title
            text_position = self.position + Vector2(int(3 * (self.__header_margins.x / 4)),
                                                    int(3 * (self.__header_margins.y / 4)))
            Drawer.draw_text(text_position, self.text, self.window)
            self.printer.print_once(
                self.id + " content zone is " + panel_content.to_string() + ". The header zone is " +
                header_zone.to_string() + ". The text is drawn on " + text_position.to_string())
