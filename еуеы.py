import time

import arcade

RIGHT_FACING = 0
LEFT_FACING = 1


class Bomb(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/tiles/bomb.png', 0.25)

    def update(self):
        self.center_x += 3


def load_texture_pair(filename, x, y, width, height):
    return [arcade.load_texture(filename, x, y, width, height),
            arcade.load_texture(filename, x, y, width, height, flipped_horizontally=True)]


class Player(arcade.Sprite):
    def __init__(self, scale=1):
        super().__init__(scale=scale)
        self.person_face_direction = RIGHT_FACING
        self.run_texture = []
        self.idle_texture = []
        self.jump_texture = []
        for i in range(10):
            texture = load_texture_pair(f"env/sprite/Colour1/Outline/120x80_PNGSheets/_Run.png", x=i * 120, y=0,
                                        width=120, height=80)
            self.run_texture.append(texture)
            texture = load_texture_pair(f"env/sprite/Colour1/Outline/120x80_PNGSheets/_Idle.png", x=i * 120, y=0,
                                        width=120, height=80)
            self.idle_texture.append(texture)
        for i in range(3):
            texture = load_texture_pair(f"env/sprite/Colour1/Outline/120x80_PNGSheets/_Jump.png", x=i * 120, y=0,
                                        width=120, height=80)
            self.jump_texture.append(texture)
        self.current_texture = 0
        self.chetjump = 0
        # self.idle_texture = load_texture_pair(f"env/sprite/Colour1/Outline/120x80_PNGSheets/_Idle.png", x=0, y=0,
        #                                       width=120, height=80)
        self.texture = self.idle_texture[0][self.person_face_direction]
        self.start = time.time()
        # self.scale=scale

    def update_animation(self, delta_time: float = 1 / 60):

        if self.change_x < 0 and self.person_face_direction == RIGHT_FACING:
            self.person_face_direction = LEFT_FACING
        if self.change_x > 0 and self.person_face_direction == LEFT_FACING:
            self.person_face_direction = RIGHT_FACING
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture[self.current_texture][self.person_face_direction]
        elif abs(self.change_x) > 0 and self.change_y == 0:
            self.texture = self.run_texture[self.current_texture][self.person_face_direction]
        elif self.change_y > 0:
            self.texture = self.jump_texture[self.chetjump][self.person_face_direction]

        if time.time() - self.start > 0.05:
            self.current_texture += 1
            self.chetjump += 1
            self.start = time.time()
        if self.current_texture >= 10:
            self.current_texture = 0
        if self.chetjump >= 3:
            self.chetjump = 0


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=640, title="Simple platformer", resizable=True)
        # self.background_texture = arcade.load_texture()
        self.scene = arcade.Scene()  # Сцена хранит списки спрайтов
        self.player = Player(3)
        # self.enemy = arcade.Sprite(':resources:images/animated_characters/zombie/zombie_idle.png')
        self.exit_table = arcade.Sprite(':resources:images/tiles/signExit.png')
        self.camera = arcade.Camera(self.width, self.height)
        self.enemy_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.plat_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.s = 0

    def on_draw(self):
        self.clear()
        arcade.draw_text(f"{self.player.position}", self.width / 2, self.height / 2, font_size=80)
        # arcade.draw_lrwh_rectangle_textured(0, 0, 3200, 1000, self.background_texture)
        self.scene.draw()
        self.enemy_list.draw()
        self.camera.use()
        self.bomb_list.draw()
        self.coin_list.draw()

    def on_update(self, delta_time: float):
        self.physics_engine.update()
        self.center_camera_to_player()
        self.enemy_list.update()
        self.bomb_list.update()
        self.box_list.update()
        self.plat_list.update()
        self.coin_list.update()
        self.player.update_animation()
        # for enemy in self.enemy_list:
        #     enemy.center_x += enemy.change_x
        #     touch_enemy_list = arcade.check_for_collision_with_list(enemy, self.box_list)
        #     if touch_enemy_list:
        #         enemy.change_x *= -1
        #     death_list = arcade.check_for_collision_with_list(self.player, self.enemy_list)
        #     if death_list:
        #         enemy.kill()
        #         print("Game over")
        #         self.close()
        touch = arcade.check_for_collision(self.player, self.exit_table)
        if touch:
            print("Win")
            self.close()
        for bomb in self.bomb_list:
            hit_list = arcade.check_for_collision_with_list(bomb, self.enemy_list)
            if hit_list:
                bomb.kill()
                for enemy in hit_list:
                    enemy.kill()
        for plat in self.plat_list:
            plat.center_y += plat.change_y
            if plat.center_y == 400 or plat.center_y == 96:
                plat.change_y *= -1
        for coin in self.coin_list:
            touch_coin_list = arcade.check_for_collision(self.player, coin)
            if touch_coin_list:
                coin.kill()
        if self.player.center_x <= self.player.width / 2:
            self.player.center_x = self.player.width / 2
        for bomb in self.bomb_list:
            if bomb.center_x >= self.player.center_x + 300:
                bomb.kill()

    def setup(self):
        # Создадим списки спрайтов на сцене
        self.scene.add_sprite_list('Enemy')
        self.scene.add_sprite_list('Walls')
        self.scene.add_sprite_list('ExitTable')
        self.scene.add_sprite_list('Player')
        # Добавляем табличку на сцену
        self.exit_table.position = 2300, 128
        self.box_list.append(self.exit_table)
        self.scene.add_sprite('Exit_table', self.exit_table)
        # Добавляем игрока на сцену
        self.player.position = 110, 128
        self.scene.add_sprite('Player', self.player)
        # Добавляем траву на сцену
        for x in range(0, 3200, 64):
            grass = arcade.Sprite(':resources:images/tiles/dirtMid.png', 0.5)
            grass.left = x
            grass.bottom = 0
            self.scene.add_sprite('Walls', grass)
        # Добавляем зомби на сцену
        coordinate_list_1 = [[375, 128], [650, 128], [900, 128]]
        for coordinate in coordinate_list_1:
            zombie = arcade.Sprite(':resources:images/animated_characters/zombie/zombie_idle.png')
            zombie.position = coordinate
            zombie.change_x = 1
            self.enemy_list.append(zombie)
        # Добавляем ящики на сцену
        coordinate_list_2 = [[235, 96], [512, 96], [760, 96]]
        for coordinate in coordinate_list_2:
            box = arcade.Sprite(':resources:images/tiles/boxCrate_double.png', 0.5)
            box.position = coordinate
            self.box_list.append(box)
            self.scene.add_sprite('Walls', box)
        # Добавляем платформу на сцену
        plat_1 = arcade.Sprite(':resources:images/tiles/dirtMid.png', 0.5)
        plat_1.position = 1200, 96
        plat_1.change_y = 1
        self.plat_list.append(plat_1)
        self.scene.add_sprite('Walls', plat_1)
        plat_2 = arcade.Sprite(':resources:images/tiles/dirtLeft.png', 0.5)
        plat_2.right = plat_1.left
        plat_2.center_y = 96
        plat_2.change_y = 1
        self.plat_list.append(plat_2)
        self.scene.add_sprite('Walls', plat_2)
        plat_3 = arcade.Sprite(':resources:images/tiles/dirtRight.png', 0.5)
        plat_3.left = plat_1.right
        plat_3.center_y = 96
        plat_3.change_y = 1
        self.plat_list.append(plat_3)
        self.scene.add_sprite('Walls', plat_3)
        # Добавляем верхнюю дорожку на сцену
        for x in range(0, 700, 64):
            grass = arcade.Sprite(':resources:images/tiles/dirtMid.png', 0.5)
            grass.left = 1392 + x
            grass.center_y = 400
            self.scene.add_sprite('Walls', grass)
            if self.s == 0:
                grass_2 = arcade.Sprite(':resources:images/tiles/dirtLeft.png', 0.5)
                grass_2.right = 1392
                grass_2.center_y = 400
                self.scene.add_sprite('Walls', grass_2)
            self.s += 1
            # Добавляем монетки
            if x % 5 == 0:
                coin = arcade.Sprite(':resources:images/items/coinGold.png')
                coin.bottom = grass.top + 10
                coin.center_x = grass.center_x
                self.coin_list.append(coin)
        grass_3 = arcade.Sprite(':resources:images/tiles/dirtRight.png', 0.5)
        grass_3.left = 2096
        grass_3.center_y = 400
        self.scene.add_sprite('Walls', grass_3)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, walls=self.scene['Walls'], gravity_constant=1)

    def center_camera_to_player(self):
        screen_center_x_1 = self.player.center_x - self.camera.viewport_width / 2
        screen_center_y_1 = self.player.center_y - self.camera.viewport_height / 2
        if screen_center_x_1 < 0:
            screen_center_x_1 = 0
        if screen_center_y_1 < 0:
            screen_center_y_1 = 0
        self.camera.move_to((screen_center_x_1, screen_center_y_1))

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x += 5
        if symbol == arcade.key.LEFT:
            self.player.change_x -= 5
        if symbol == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 20

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 0
        if symbol == arcade.key.LEFT:
            self.player.change_x = 0
        if symbol == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            bomb = Bomb()
            bomb.center_x = self.player.center_x
            bomb.center_y = self.player.top
            self.bomb_list.append(bomb)


window = MyWindow()
window.setup()
arcade.run()
