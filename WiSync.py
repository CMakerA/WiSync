from UI import *

window = Window(Size(1000, 700), "WiSync", "logo.png")

panel = Panel(Position(10, 10), Size(100, 50), Colors.flat_red)
window.add(panel)

button1 = Button(Size(80, 25), Position(5, 5), "Button1", UIThemes.light)
panel.add(button1)

window.start()
