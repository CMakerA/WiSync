from UI import *

window = Window(Size(1000, 700), "Window", "logo.png")

button1 = Button(Size(50, 30), Position(10, 10), UIThemes.dark)
window.add(button1)

window.start()
