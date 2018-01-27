from UI import *


def btn1click():
    print("Clicked btn 1")


window = Window(Vector2(700, 500), "Wi Sync", Colors.dark_gray)
panel = HeaderPanel(Vector2(30, 30), Vector2(200, 180), "Panel Header")
window.add(panel)
button1 = Button("Button 1", Vector2(10, 10), Vector2(0, 0), btn1click)
window.add(button1)

window.start()
