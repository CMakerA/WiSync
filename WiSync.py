from UI import *

window = Window(Size(1000, 700), "WiSync", "logo.png")

panel = Panel(Position(10, 10), Size(160, 55), Colors.flat_red)
# window.add(panel)

pnl_btn1 = Button(Size(140, 35), Position(10, 10), "Button Panel Light", UIThemes.light)
# panel.add(pnl_btn1)

textbox = TextBox(Size(150, 40), Position(10, 10), "")
window.add(textbox)

window.start()
