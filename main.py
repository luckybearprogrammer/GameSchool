import arcade


class Window(arcade.Window):
    def __init__(self):
        super().__init__(1000, 800, "Ем чипсЕки")
        self.bg = arcade.load_texture("env/chips.png")
        self.z = 0

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0 - self.z, 0, window.width, window.height, self.bg)
        arcade.draw_lrwh_rectangle_textured(window.width - self.z, 0, window.width, window.height, self.bg)
        self.z += 5
        if self.z > window.width:
            self.z = 0


window = Window()
arcade.run()
