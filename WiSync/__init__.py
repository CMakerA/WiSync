from elements import *
from Dimensions import *
from Color import *

window = Window(Size(1000, 700), "WiSync", None)

panel = Panel(Position(10, 10), Size(160, 55), Colors.flat_red)
# window.add(panel)

button = Button(Size(100, 35), Position(20, 20), "Button Light", UIThemes.light)
window.add(button)

textbox = TextBox(Size(150, 40), Position(10, 10), "textbox")
# window.add(textbox)

window.start()
