import arcade
from arcade import load_texture
from arcade.gui import UIManager
from arcade.gui.widgets import UITextArea, UIInputText, UITexturePane
from serclient import *
formatted_lorem_ipsum = ""
max_length = 0
names = []
numbers = []
a = top()
for line in a:
    if line:
        parts = line.split()
        if len(parts) == 2:
            name, number = parts
            names.append(name)
            numbers.append(number)
            max_length = max(max_length, len(name))
max_length += 20
a.pop(-1)
for line in a:
    formatted_lorem_ipsum += line.split()[0] + " " * (max_length - len(line)) + line.split()[1] + "\n\n"

print(formatted_lorem_ipsum)


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(1980, 1080, "Scrollable Text", resizable=True)
        self.bg = arcade.load_texture("env/liders.png")
        self.manager = UIManager()
        self.manager.enable()
        self.font = arcade.load_font("env/DischargePro.ttf")
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        bg_tex = load_texture("env/bgliders.png")
        text_area = UITextArea(x=500,
                               y=200,
                               width=1500,
                               height=800,
                               text=formatted_lorem_ipsum,
                               text_color=arcade.color.GOLD,
                               font_size=50,
                               font_name="Discharge Pro")
        self.manager.add(
            UITexturePane(
                text_area.with_space_around(),
                tex=bg_tex,
            )
        )

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, window.width, window.height, self.bg)
        self.manager.draw()


window = MyWindow()
arcade.run()
