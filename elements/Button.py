from UIElement import *
from style.Style import *


class Button(InteractableUIElement):
    __idle = Styles.blue_button
    __hover = Styles.red_button
    __click = Style(Colors.yellow, Colors.transparent, Colors.transparent, 0, 30)

    __font_margin = 15

    def __init__(self, btn_text: str, position: Vector2, size: Vector2 = None, on_click=None, on_hover=None,
                 on_leave=None):
        text_size = 20
        self.text = Font.create_text(btn_text, self.font_preferences, text_size, self.__idle.text_color.get())
        if size is None:
            self.size = Vector2(text_size + (self.__font_margin * 2),
                                (text_size * len(btn_text)) + (self.__font_margin * 2))
        else:
            self.size = size

        super().__init__(position, self.__idle, self.__hover, self.__click, self.size, on_click, on_hover, on_leave)

        self.id = Iders.btnIdler.add(self)

        print("Initialized Button with id " + self.id + ", in coordinates (" + str(position.x) + ", " + str(
            position.y) + "), with size(" + str(self.size.x) + ", " + str(self.size.y) + ")")

    def get_window(self):
        return self.window

    def draw(self, starting_point: Vector2 = None):
        super().draw(starting_point)
        if self.window is not None:
            if starting_point is None:
                Drawer.draw_text(self.position + Vector2(int(self.__font_margin - (20 / 100 * self.__font_margin))),
                                 self.text, self.window)
            else:
                Drawer.draw_text(starting_point + (
                        self.position + Vector2(int(self.__font_margin - (20 / 100 * self.__font_margin)))),
                                 self.text, self.window)
