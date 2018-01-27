from UI import *
import Font

window = Window(Vector2(500, 300), "New Window", Color.hex_to_rgb("#81ecec"))
button1 = Button(Font.create_text("Button 1", Font.openSans_preferences, 20, Colors.black.get()), Vector2(100, 45), Vector2(0, 0))
window.add(button1)

window.start()