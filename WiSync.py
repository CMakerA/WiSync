from UI import *

window = Window(Size(1000, 700), "WiSync", "logo.png")

# panel = Panel(Position(10, 10), Size(200, 160), Colors.flat_red)
# window.add(panel)

pnl_btn1 = Button(Size(130, 25), Position(10, 10), "Button Panel Light", UIThemes.light)
window.add(pnl_btn1)

window.start()
