import arcade
from arcade import load_texture
from arcade.gui import UIManager
from arcade.gui.widgets import UITextArea, UIInputText, UITexturePane

LOREM_IPSUM = (
    "0 Mike\n\n"
    "21312 Lox\n\n"
    "213123 dfds\n\n"
    "2131231221312 dsfdsf\n\n"
    "23213123213 efefew\n\n"
    "0 Mike\n\n"
    "0 Mike\n\n"
    "21312 Lox\n\n"
    "213123 dfds\n\n"
    "2131231221312 dsfdsf\n\n"
    "23213123213 efefew\n\n"
    "0 Mike\n\n"
    "0 Mike\n\n"
    "21312 Lox\n\n"
    "213123 dfds\n\n"
    "2131231221312 dsfdsf\n\n"
    "23213123213 efefew\n\n"
    "0 Mike\n\n")


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Scrollable Text", resizable=True)
        self.bg = arcade.load_texture("env/liders.png")
        self.manager = UIManager()
        self.manager.enable()
        self.font = arcade.load_font("env/DischargePro.ttf")
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        bg_tex = load_texture("env/bgliders.png")
        text_area = UITextArea(x=1000,
                               y=300,
                               width=1000,
                               height=800,
                               text=LOREM_IPSUM,
                               text_color=arcade.color.RED,
                               font_size=50,
                               font_name="Discharge Pro")
        self.manager.add(
            UITexturePane(
                text_area.with_space_around(right=20),
                tex=bg_tex,
                padding=(10, 10, 10, 10),

            )
        )

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, window.width, window.height, self.bg)
        self.manager.draw()


window = MyWindow()
arcade.run()
