import random

import arcade
import webbrowser
from weather import get_current_weather
import arcade.gui
from serclient import *

LANGUAGE = "rus"
music = arcade.play_sound(arcade.load_sound("env/bgmusic.mp3"), looping=True)


# music.volume=0

class StartView(arcade.View):
    def __init__(self):
        super().__init__()
        self.bg = arcade.load_texture("env/Default.png")
        self.bg1 = arcade.load_texture("env/Default.png")
        self.bgShadow = arcade.load_texture("env/Shadow.png")
        self.bgChips = arcade.load_texture("env/chips.png")
        self.exitTexture = arcade.load_texture("env/exit.png")
        self.optinonsTexture = arcade.load_texture("env/options.png")
        self.iconVk = arcade.load_texture("env/vk-logo.png")
        self.startButton = arcade.load_texture("env/cartoon-crystal-ui-collection_52683-73194_1.png", x=785, y=40,
                                               width=270, height=95)
        self.exitButton = arcade.load_texture("env/cartoon-crystal-ui-collection_52683-73194_1.png", x=1055, y=40,
                                              width=270, height=95)
        self.optinonsButton = arcade.load_texture("env/cartoon-crystal-ui-collection_52683-73194_1.png", x=785,
                                                  y=40 + 95 * 3 + 10,
                                                  width=270, height=95)
        self.quest = arcade.load_texture("env/question.png")
        self.scaleOfQuest = 0.1
        self.ButtonScale = 1.2
        self.z = 0
        self.huh = arcade.load_sound("env/huh.mp3")
        self.font = arcade.load_font("env/DischargePro.ttf")
        with open("env/user.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == "None":
                    self.manager = arcade.gui.UIManager()
                    self.manager.enable()
                    self.l = True
                else:
                    self.l = False

    def on_click_open(self):
        message_box = arcade.gui.UIMessageBox(
            width=300,
            height=200,
            message_text=(
                "Ты должен придумать себе ник в настройках"
            ),
            callback=self.on_message_box_close,
            buttons=["Ok"]
        )

        self.manager.add(message_box)

    def on_message_box_close(self, button_text):
        print(f"User pressed {button_text}.")

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0 - self.z, 0, window.width, window.height, self.bg)
        arcade.draw_lrwh_rectangle_textured(window.width - self.z, 0, window.width, window.height, self.bg)

        arcade.draw_lrwh_rectangle_textured(window.width / 10 - self.iconVk.width / 2 * 0.05,
                                            window.height / 9 - self.iconVk.height / 2 * 0.05, self.iconVk.width * 0.05,
                                            self.iconVk.height * 0.05, self.iconVk)
        if (window.width / 10 - self.iconVk.width / 2 * 0.05 <= window._mouse_x <=
                window.width / 10 + self.iconVk.width * 0.05
                and window.height / 9 - self.iconVk.height / 2 * 0.05 <= window._mouse_y <=
                window.height / 9 + self.iconVk.height * 0.05):
            arcade.draw_lrwh_rectangle_textured(window.width / 10 - self.iconVk.width / 2 * 0.07,
                                                window.height / 9 - self.iconVk.height / 2 * 0.07,
                                                self.iconVk.width * 0.07,
                                                self.iconVk.height * 0.07, self.iconVk)
        if not self.l:
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
        else:
            self.manager.draw()
            if (window.width / 2 - self.quest.width / 2 * self.scaleOfQuest <= window._mouse_x <=
                    window.width / 2 + self.quest.width / 2 * self.scaleOfQuest and
                    window.height / 2 - self.quest.height / 2 * self.scaleOfQuest <= window._mouse_y <=
                    window.height / 2 + self.quest.height / 2 * self.scaleOfQuest):
                arcade.draw_lrwh_rectangle_textured(
                    window.width / 2 - self.quest.width / 2 * (self.scaleOfQuest + 0.05),
                    window.height / 2 - self.quest.height / 2 * (self.scaleOfQuest + 0.05),
                    self.quest.width * (self.scaleOfQuest + 0.05),
                    self.quest.height * (self.scaleOfQuest + 0.05), self.quest)
            else:
                arcade.draw_lrwh_rectangle_textured(window.width / 2 - self.quest.width / 2 * self.scaleOfQuest,
                                                    window.height / 2 - self.quest.height / 2 * self.scaleOfQuest,
                                                    self.quest.width * self.scaleOfQuest,
                                                    self.quest.height * self.scaleOfQuest, self.quest)

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

        # arcade.draw_text(temp, window.width / 7, window.height / 7,
        #                  arcade.color.WHITE, 70,
        #                  font_name="Discharge Pro", anchor_x="center")

        self.z += 3
        if self.z > window.width:
            self.z = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if not self.l and (window.width / 2 - self.startButton.width / 2 * self.ButtonScale <= x
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
        if (window.width / 10 - self.iconVk.width / 2 * 0.05 <= x <=
                window.width / 10 + self.iconVk.width * 0.05
                and window.height / 9 - self.iconVk.height / 2 * 0.05 <= y <=
                window.height / 9 + self.iconVk.height * 0.05):
            webbrowser.open("https://vk.com/blaatnoiii")
        if (window.width / 2 - self.quest.width / 2 * 0.1 <= x <=
                window.width / 2 + self.quest.width / 2 * 0.1 and
                window.height / 2 - self.quest.height / 2 * 0.1 <= y <=
                window.height / 2 + self.quest.height / 2 * 0.1):
            self.scaleOfQuest = 0.001
            self.on_click_open()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.P:
            self.window.show_view(LidersView())


class OptionsView(arcade.View):
    def __init__(self, z):
        super().__init__()
        self.bg = arcade.load_texture("env/Shadow.png")
        self.font = arcade.load_font("env/DischargePro.ttf")
        self.rus = arcade.load_texture("env/rus.png")
        self.eng = arcade.load_texture("env/eng.png")
        self.login = arcade.load_texture("env/login.png")
        self.on = arcade.load_texture("env/onoff.png", x=0, y=0, width=1146, height=503)
        self.off = arcade.load_texture("env/onoff.png", x=0, y=503, width=1146, height=503)
        self.chet = 0
        self.sizeOFFlag = 0.1
        self.z = z
        self.base = False

        with open("env/user.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == "None":
                    self.manager = arcade.gui.UIManager()
                    self.manager.enable()
                    self.l = True
                    animals = ["кенгуру", "жираф", "пингвин", "лев"]
                    self.textq = arcade.gui.UIInputText(window.width / 1.65, 0.3 * window.height,
                                                        width=window.width / 4, height=140, font_name="Discharge Pro",
                                                        text_color=arcade.color.WHITE,
                                                        font_size=80,
                                                        text=f"{animals[random.randint(0, len(animals) - 1)]}"
                                                             f"{random.randint(0, 100)}")
                    self.manager.add(self.textq)
                else:
                    self.nick = line.strip()
                    self.l = False

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
            arcade.draw_text(f"какая то настройка", window.width / 4 + window.width / 2, 0.65 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Музыка", window.width / 4, 0.5 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"какая то настройка", window.width / 4 + window.width / 2, 0.5 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Пользователь", window.width / 4, 0.35 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text("О разработчиках", window.width / 4, 0.2 * window.height,
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

        if self.l:
            self.manager.draw()
            arcade.draw_lrwh_rectangle_textured(window.width / 4 + window.width / 2 - self.login.width / 2 * 0.2,
                                                0.15 * window.height,
                                                self.login.width * 0.2,
                                                self.login.height * 0.2, self.login)
        else:
            arcade.draw_text(self.nick, window.width / 4 + window.width / 2, 0.35 * window.height,
                             font_name="Discharge Pro",
                             color=arcade.color.GREEN, anchor_x="center",
                             font_size=80)
        if self.base:
            arcade.draw_text("ник занят", window.width / 4 + window.width / 2, 0.1 * window.height,
                             font_name="Discharge Pro",
                             color=arcade.color.RED, anchor_x="center",
                             font_size=80)

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
        if self.chet % 2 == 0:
            arcade.draw_lrwh_rectangle_textured(window.width / 2.8,
                                                0.5 * window.height,
                                                self.on.width * 0.15,
                                                self.on.height * 0.15,
                                                self.on)
        else:
            arcade.draw_lrwh_rectangle_textured(window.width / 2.8,
                                                0.5 * window.height,
                                                self.on.width * 0.15,
                                                self.on.height * 0.15,
                                                self.off)

        self.z += 3
        if self.z > window.width:
            self.z = 0

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            start_view.z = self.z
            self.window.show_view(start_view)
        if symbol == arcade.key.D:
            webbrowser.open("https://github.com/luckybearprogrammer")

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
        if (window.width / 4 + window.width / 2 - self.login.width / 2 * 0.2 <= x <= window.width / 4 +
                window.width / 2 - self.login.width / 2 * 0.2 + self.login.width * 0.2 and
                0.15 * window.height <= y <= 0.15 * window.height + self.login.height * 0.2):
            if can(str(self.textq.text)):
                print(f"да, ник {self.textq.text} не занят")
                with open("env/user.txt", "w", encoding="utf-8") as file:
                    file.write(self.textq.text)
                self.nick = self.textq.text
                self.l = False
                self.base = False
                start_view.l = False
            else:
                self.base = True
        if window.width / 2.8 <= x <= window.width / 2.8 + self.on.width * 0.15 and 0.5 * window.height <= 0.5 * window.height + self.on.height:
            global music
            if self.chet % 2 != 0:
                music.volume = 1
            else:
                music.volume = 0
            self.chet += 1


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


class LidersView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.font = arcade.load_font("env/DischargePro.ttf")
        self.bg = arcade.load_texture("env/liders.png")
        bg_tex = arcade.load_texture("env/bgliders.png")

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

        text_area = arcade.gui.UITextArea(x=500,
                                          y=200,
                                          width=1500,
                                          height=800,
                                          text=formatted_lorem_ipsum,
                                          text_color=arcade.color.GOLD,
                                          font_size=50,
                                          font_name="Discharge Pro")
        self.manager.add(
            arcade.gui.UITexturePane(
                text_area.with_space_around(),
                tex=bg_tex,
            )
        )

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, window.width, window.height, self.bg)
        self.manager.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.window.show_view(start_view)


window = arcade.Window(1980, 1080, resizable=True)

# window = arcade.Window(fullscreen=True)
start_view = StartView()
chipsView = ChipsView()
optView = OptionsView(0)
window.show_view(start_view)
arcade.run()
# тест
