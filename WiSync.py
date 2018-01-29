from UI import *

window = Window(Size(1000, 700), "WiSync", "logo.png")

button1 = Button(Size(80, 25), Position(10, 10), "Button1", UIThemes.light)
window.add(button1)

window.start()
