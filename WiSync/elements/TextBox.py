from Dimensions import *
from Style import *
from Font import *
from Ider import *
import Drawer
from elements.UIElement import *
import Time
import pygame
import Cursors

class TextBox(UIElement):
    __blink_time = 500  # In millis

    def __init__(self, size: Size, position: Position, text: str, font: Font = None,
                 password_char: str = None):
        self.position = position
        self.size = size
        self.text = text
        if font is None:
            self.font = Font(Fonts.comic_sans.name, 15)
        else:
            self.font = font
        self.password_char = password_char

        self.elements = list()

        super().__init__("txt", self.size, self.position)

        self.style = Styles.text_box

        self.__last_blink_time = Time.millis()

        self.event_handler = self.__event_handler

        self.focused_border = BorderStyle(self.style.focused_border_color, self.style.focused_border_width)
        self.unfocused_border = BorderStyle(self.style.border_color, self.style.border_width)

    def add(self, element: UIElement):
        self.elements.append(element)

    focused = False

    __last_blink_shown = False

    def __event_handler(self, event: pygame.event):
        if self.focused:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.text += " "
                elif event.key == pygame.K_BACKSLASH or event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    text = str(self.text[:-1])
                    self.text = text
                    self.window_class.draw_again()
                else:
                    self.text += event.unicode
                self.draw()
                print(self.id + " text is \"" + self.text + "\"")

    shown_focus = False
    shown_unfocus = False
    wait_for_unclick = False

    def draw(self, start_position: Vector2 = None):
        Printer.print_once("Initialized " + self.id + " in " + self.position.to_string() + " with size " +
                           self.size.to_string() + ". " + self.zone.to_string())

        hitbox = Zone.zone_correction(self.zone, self.focused_border.width)

        if hitbox.point_over(Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
            pygame.mouse.set_cursor(*Cursors.text_select)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

        if pygame.mouse.get_pressed()[0]:
            if not self.wait_for_unclick:
                self.wait_for_unclick = True
                if hitbox.point_over(Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
                    if not self.shown_focus:
                        print("Focused " + self.id)
                    self.focused = True
                    self.shown_unfocus = False
                    self.shown_focus = True
                elif not self.zone.point_over(Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
                    if not self.shown_unfocus:
                        print("Unfocused " + self.id)
                    self.focused = False
                    self.shown_unfocus = True
                    self.shown_focus = False
        else:
            self.wait_for_unclick = False

        if self.focused:
            Drawer.draw_rounded_border_rect(self.zone, self.style.focused_background_color, self.focused_border,
                                            self.window)

            # <editor-fold desc="Show cursor">
            if Time.millis() - self.__last_blink_shown > self.__blink_time:
                if self.__last_blink_shown:
                    # draw down line
                    pass
                else:
                    # don't draw line
                    pass
                self.__last_blink_shown = not self.__last_blink_shown
            # </editor-fold>
        else:
            Drawer.draw_rounded_border_rect(self.zone, self.style.background_color, self.unfocused_border, self.window)

        if self.password_char is not None:
            Drawer.draw_text(self.zone.vector1 + Vector2(5, 5), Colors.black, self.password_char * len(self.text),
                             self.font, self.window)
        else:
            Drawer.draw_text(self.zone.vector1 + Vector2(5, 5), Colors.black, self.text, self.font, self.window)