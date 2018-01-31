from UI import *

window = Window(Size(300, 135), "Sample login form")

name_label = Label(Position(10, 5), "Username:", Colors.white, Fonts.comic_sans.size(20))

name_textbox = TextBox(Size(150, 40), Position(10, 35), "")

password_label = Label(Position(170, 5), "Password:", Colors.white, Fonts.comic_sans.size(20))

password_textbox = TextBox(Size(150, 40), Position(170, 35), "", None, "*")

button = Button(Size(280, 35), Position(10, 85), "Login", UIThemes.light)
window.add(button)

window.add(name_label)
window.add(name_textbox)
window.add(password_label)
window.add(password_textbox)

window.start()
