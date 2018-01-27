from UI import *


def btn1click():
    print("Clicked btn 1")


window = Window(Vector2(700, 500), "New Window", Colors.aqua_blue)
# button1 = Button("Button 1", Vector2(100, 45), Vector2(0, 0), btn1click)
# window.add(button1)
panel = HeaderPanel(Vector2(30, 30), Vector2(0, 0), "Header")
window.add(panel)

window.start()
