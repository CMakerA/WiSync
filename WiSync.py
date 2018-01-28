from UI import *


def button1_click():
    print("Clicked btn1")


window = Window(Vector2(700, 500), "Wi Sync", Colors.dark_gray)
panel = HeaderPanel(Position(30, 30), Size(200, 180), "Header")
# window.add(panel)
button1 = Button("Button 1", Position(10, 10), Size(100, 30), button1_click())
window.add(button1)

window.start()
