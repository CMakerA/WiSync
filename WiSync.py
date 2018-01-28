from UI import *

window = Window(Size(1000, 700), "WiSync", "logo.png")

button1 = Button(Size(50, 30), Position(10, 10), UIThemes.dark)
window.add(button1)

Drawer.draw_rect(button1.zone, button1.current_color, window.screen)

window.start()
