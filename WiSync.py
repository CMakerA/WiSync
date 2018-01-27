from UI import *
from elements.Button import *
from elements.HeaderPanel import *
from elements.Panel import *


window = Window(Vector2(700, 500), "Wi Sync", Colors.dark_gray)
panel = HeaderPanel(Vector2(30, 30), Vector2(200, 180), "Panel Header")
window.add(panel)
button1 = Button("Button 1", Vector2(10, 10), Vector2(100, 30), print("Clicked btn 1"))
window.add(button1)

window.start()
