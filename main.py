import arcade

LANGUAGE = "rus"


class StartView(arcade.View):
    def __init__(self):
        super().__init__()
        self.bg = arcade.load_texture("env/Default.png")
        self.bgShadow = arcade.load_texture("env/Shadow.png")
        self.startButton = arcade.load_texture("env/cartoon-crystal-ui-collection_52683-73194_1.png", x=785, y=40,
                                               width=270, height=95)
        self.exitButton = arcade.load_texture("env/cartoon-crystal-ui-collection_52683-73194_1.png", x=1055, y=40,
                                              width=270, height=95)
        self.optinonsButton = arcade.load_texture("env/cartoon-crystal-ui-collection_52683-73194_1.png", x=785,
                                                  y=40 + 95 * 3 + 10,
                                                  width=270, height=95)
        self.ButtonScale = 1.2
        self.z = 0
        self.huh = arcade.load_sound("env/huh.mp3")
        self.font = arcade.load_font("env/DischargePro.ttf")

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0 - self.z, 0, window.width, window.height, self.bg)
        arcade.draw_lrwh_rectangle_textured(window.width - self.z, 0, window.width, window.height, self.bg)
        if not (window.width / 2 - self.startButton.width / 2 * self.ButtonScale <= window._mouse_x
                <= window.width / 2 + self.startButton.width / 2 * self.ButtonScale
                and
                window.height / 2 - self.startButton.height / 2 * self.ButtonScale <= window._mouse_y
                <= window.height / 2 + self.startButton.height / 2 * self.ButtonScale):
            arcade.draw_lrwh_rectangle_textured(window.width / 2 - self.startButton.width / 2 * self.ButtonScale,
                                                window.height / 2 - self.startButton.height / 2 * self.ButtonScale,
                                                self.startButton.width * self.ButtonScale,
                                                self.startButton.height * self.ButtonScale, self.startButton)
        else:
            arcade.draw_lrwh_rectangle_textured(
                window.width / 2 - self.startButton.width / 2 * (self.ButtonScale + 0.3),
                window.height / 2 - self.startButton.height / 2 * (self.ButtonScale + 0.3),
                self.startButton.width * (self.ButtonScale + 0.3),
                self.startButton.height * (self.ButtonScale + 0.3), self.startButton)
        if not (window.width / 2 - self.startButton.width / 2 * self.ButtonScale <= window._mouse_x
                <= window.width / 2 + self.startButton.width / 2 * self.ButtonScale
                and
                window.height / 2 - self.startButton.height / 2 * self.ButtonScale - 0.15 * window.height <= window._mouse_y
                <= window.height / 2 + self.startButton.height / 2 * self.ButtonScale - 0.15 * window.height):
            arcade.draw_lrwh_rectangle_textured(window.width / 2 - self.startButton.width / 2 * self.ButtonScale,
                                                window.height / 2 - self.startButton.height / 2 * self.ButtonScale - 0.15 * window.height,
                                                self.startButton.width * self.ButtonScale,
                                                self.startButton.height * self.ButtonScale, self.optinonsButton)
        else:
            arcade.draw_lrwh_rectangle_textured(
                window.width / 2 - self.startButton.width / 2 * (self.ButtonScale + 0.3),
                window.height / 2 - self.startButton.height / 2 * (self.ButtonScale + 0.3) - 0.15 * window.height,
                self.startButton.width * (self.ButtonScale + 0.3),
                self.startButton.height * (self.ButtonScale + 0.3), self.optinonsButton)

        if not (window.width / 2 - self.startButton.width / 2 * self.ButtonScale <= window._mouse_x
                <= window.width / 2 + self.startButton.width / 2 * self.ButtonScale
                and
                window.height / 2 - self.startButton.height / 2 * self.ButtonScale - 0.3 * window.height <= window._mouse_y
                <= window.height / 2 + self.startButton.height / 2 * self.ButtonScale - 0.3 * window.height):
            arcade.draw_lrwh_rectangle_textured(window.width / 2 - self.startButton.width / 2 * self.ButtonScale,
                                                window.height / 2 - self.startButton.height / 2 * self.ButtonScale - 0.3 * window.height,
                                                self.startButton.width * self.ButtonScale,
                                                self.startButton.height * self.ButtonScale, self.exitButton)
        else:
            arcade.draw_lrwh_rectangle_textured(
                window.width / 2 - self.startButton.width / 2 * (self.ButtonScale + 0.3),
                window.height / 2 - self.startButton.height / 2 * (self.ButtonScale + 0.3) - 0.3 * window.height,
                self.startButton.width * (self.ButtonScale + 0.3),
                self.startButton.height * (self.ButtonScale + 0.3), self.exitButton)
        global LANGUAGE
        if LANGUAGE == "rus":
            arcade.draw_text(f"Приключение Степиды и его кентов", window.width / 2, 0.65 * window.height,
                             arcade.color.WHITE, 70,
                             font_name="Discharge Pro", anchor_x="center")
        else:
            arcade.draw_text(f"The adventure of StepanIA and his Kents", window.width / 2, 0.65 * window.height,
                             arcade.color.WHITE, 70,
                             font_name="Discharge Pro", anchor_x="center")

        self.z += 3
        if self.z > window.width:
            self.z = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if (window.width / 2 - self.startButton.width / 2 * self.ButtonScale <= x
                <= window.width / 2 + self.startButton.width / 2 * self.ButtonScale
                and
                window.height / 2 - self.startButton.height / 2 * self.ButtonScale <= y
                <= window.height / 2 + self.startButton.height / 2 * self.ButtonScale):
            arcade.play_sound(self.huh)
            global chipsView
            self.window.show_view(chipsView)
        if (window.width / 2 - self.startButton.width / 2 * self.ButtonScale <= x
                <= window.width / 2 + self.startButton.width / 2 * self.ButtonScale
                and
                window.height / 2 - self.startButton.height / 2 * self.ButtonScale - 0.15 * window.height <= y
                <= window.height / 2 + self.startButton.height / 2 * self.ButtonScale - 0.15 * window.height):
            global optView
            optView.z = self.z
            self.window.show_view(optView)
        if (window.width / 2 - self.startButton.width / 2 * self.ButtonScale <= x
                <= window.width / 2 + self.startButton.width / 2 * self.ButtonScale
                and
                window.height / 2 - self.startButton.height / 2 * self.ButtonScale - 0.3 * window.height <= y
                <= window.height / 2 + self.startButton.height / 2 * self.ButtonScale - 0.3 * window.height):
            arcade.play_sound(self.huh)
            arcade.exit()


class OptionsView(arcade.View):
    def __init__(self, z):
        super().__init__()
        self.bg = arcade.load_texture("env/Shadow.png")
        self.font = arcade.load_font("env/DischargePro.ttf")
        self.rus = arcade.load_texture("env/rus.png")
        self.eng = arcade.load_texture("env/eng.png")
        self.sizeOFFlag = 0.1
        self.z = z

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0 - self.z, 0, window.width, window.height, self.bg)
        arcade.draw_lrwh_rectangle_textured(window.width - self.z, 0, window.width, window.height, self.bg)
        if LANGUAGE == "rus":
            arcade.draw_text(f"Настройки", window.width / 2, 0.84 * window.height,
                             arcade.color.WHITE, 80,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Язык", window.width / 4, 0.65 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Режим барана", window.width / 4 + window.width / 2, 0.65 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Музыка", window.width / 4, 0.5 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Бимбимбамбам", window.width / 4 + window.width / 2, 0.5 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text("О разработчиках", window.width / 2, 0.35 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
        else:
            arcade.draw_text(f"Options", window.width / 2, 0.84 * window.height,
                             arcade.color.WHITE, 80,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Language", window.width / 4, 0.65 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Ram mode", window.width / 4 + window.width / 2, 0.65 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Music", window.width / 4, 0.5 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Python is trash", window.width / 4 + window.width / 2, 0.5 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
        arcade.draw_lrwh_rectangle_textured(window.width / 4 + 0.1 * window.width,
                                            0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag,
                                            self.rus.width * self.sizeOFFlag,
                                            self.rus.height * self.sizeOFFlag, self.rus)
        arcade.draw_lrwh_rectangle_textured(window.width / 4 + 0.2 * window.width,
                                            0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag,
                                            self.rus.width * self.sizeOFFlag,
                                            self.rus.height * self.sizeOFFlag, self.eng)
        if (window.width / 4 + 0.1 * window.width <= window._mouse_x
                <= window.width / 4 + 0.1 * window.width + self.rus.width * self.sizeOFFlag and
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag <= window._mouse_y <=
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag + self.rus.height * self.sizeOFFlag):
            arcade.draw_lrwh_rectangle_textured(window.width / 4 + 0.1 * window.width,
                                                0.67 * window.height - self.rus.height / 2 * (self.sizeOFFlag + 0.04),
                                                self.rus.width * (self.sizeOFFlag + 0.04),
                                                self.rus.height * (self.sizeOFFlag + 0.04), self.rus)
        if (window.width / 4 + 0.2 * window.width <= window._mouse_x
                <= window.width / 4 + 0.2 * window.width + self.rus.width * self.sizeOFFlag and
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag <= window._mouse_y <=
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag + self.rus.height * self.sizeOFFlag):
            arcade.draw_lrwh_rectangle_textured(window.width / 4 + 0.2 * window.width,
                                                0.67 * window.height - self.rus.height / 2 * (self.sizeOFFlag + 0.04),
                                                self.rus.width * (self.sizeOFFlag + 0.04),
                                                self.rus.height * (self.sizeOFFlag + 0.04), self.eng)

        self.z += 3
        if self.z > window.width:
            self.z = 0

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            start_view.z = self.z
            self.window.show_view(start_view)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        global LANGUAGE
        if (window.width / 4 + 0.1 * window.width <= x
                <= window.width / 4 + 0.1 * window.width + self.rus.width * self.sizeOFFlag and
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag <= y <=
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag + self.rus.height * self.sizeOFFlag):
            LANGUAGE = "rus"
        if (window.width / 4 + 0.2 * window.width <= window._mouse_x
                <= window.width / 4 + 0.2 * window.width + self.rus.width * self.sizeOFFlag and
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag <= window._mouse_y <=
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag + self.rus.height * self.sizeOFFlag):
            LANGUAGE = "eng"


class ChipsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.bg = arcade.load_texture("env/chips.png")
        self.z = 0
        self.huh = arcade.load_sound("env/huh.mp3")

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0 - self.z, 0, window.width, window.height, self.bg)
        arcade.draw_lrwh_rectangle_textured(window.width - self.z, 0, window.width, window.height, self.bg)
        self.z += 5
        if self.z > window.width:
            self.z = 0

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.play_sound(self.huh)
            self.window.show_view(start_view)


# window = arcade.Window(1980,1080)

window = arcade.Window(fullscreen=True)
start_view = StartView()
chipsView = ChipsView()
optView = OptionsView(0)
window.show_view(start_view)
arcade.run()
# тест
