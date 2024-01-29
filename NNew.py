import arcade
import time

RIGHT_FACING = 0
LEFT_FACING = 1


def load_texture_pair(filename, x, y, width, height):
    return [arcade.load_texture(filename, x, y, width, height),
            arcade.load_texture(filename, x, y, width, height, flipped_horizontally=True)]


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(scale=3)
        self.person_face_direction = RIGHT_FACING
        self.run_texture = []
        for i in range(10):
            arcade.load_texture("Colour1/Outline/120x80_PNGSheets/_Run.png")
            texture = load_texture_pair(f"Colour1/Outline/120x80_PNGSheets/_Run.png", x=i * 120, y=0,
                                        width=120, height=80)
            self.run_texture.append(texture)
        self.current_texture = 0
        self.idle_texture = load_texture_pair(f"Colour1/Outline/120x80_PNGSheets/_Idle.png", x=0, y=0,
                                              width=120, height=80)
        self.texture = self.idle_texture[0]
        self.start = time.time()

    def update_animation(self, delta_time: float = 1 / 60):
        if self.change_x == 0:
            self.texture = self.idle_texture[self.person_face_direction]
            return
        if self.change_x < 0 and self.person_face_direction == RIGHT_FACING:
            self.person_face_direction = LEFT_FACING
        if self.change_x > 0 and self.person_face_direction == LEFT_FACING:
            self.person_face_direction = RIGHT_FACING
        self.texture = self.run_texture[self.current_texture][self.person_face_direction]
        print(time.time() - self.start)
        if time.time() - self.start > 0.05:
            self.current_texture += 1
            self.start = time.time()
        if self.current_texture >= 10:
            self.current_texture = 0


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Simple platformer", fullscreen=True)
        self.player = Player()
        self.camera = arcade.Camera(self.width, self.height)
        self.enemy_list = arcade.SpriteList()
        self.tile_map = arcade.load_tilemap("For_my_game.tmx")
        print(self.tile_map.sprite_lists)
        self.scene = arcade.Scene()
        self.background_list = arcade.SpriteList()
        self.background_list_2 = arcade.SpriteList()
        for i in self.tile_map.sprite_lists['Platforms']:
            self.scene.add_sprite('Ground', i)
        for i in self.tile_map.sprite_lists['Background']:
            self.background_list.append(i)
        for i in self.tile_map.sprite_lists['Background2']:
            self.background_list_2.append(i)
        for i in self.tile_map.sprite_lists['Enemy']:
            self.enemy_list.append(i)
        self.setup()

    def on_draw(self):
        self.clear()
        self.background_list.draw()
        self.background_list_2.draw()
        self.enemy_list.draw()
        self.scene.draw()
        self.enemy_list.draw()
        self.camera.use()
        self.player.draw()

    def on_update(self, delta_time: float):
        self.background_list.update()
        self.background_list_2.update()
        self.center_camera_to_player()
        self.player.update()
        self.scene.update()
        self.enemy_list.update()
        self.physics_engine.update()
        # self.center_camera_to_player()
        self.enemy_list.update()
        self.player.update_animation()
        if self.player.center_x <= self.player.width / 4:
            self.player.center_x = self.player.width / 4
        # if self.player.center_x >= self.width - self.player.width / 4:
        #     self.player.center_x = self.width - self.player.width / 4
        for enemy in self.enemy_list:
            death_list = arcade.check_for_collision_with_list(self.player, self.enemy_list)
            if death_list:
                enemy.kill()
                print("Game over")
                self.close()

    def setup(self):
        self.scene.add_sprite_list('Player')
        self.player.position = 50, 384
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, walls=self.scene['Ground'],
                                                             gravity_constant=1.8)

    def center_camera_to_player(self):
        screen_center_x_1 = self.player.center_x - self.camera.viewport_width / 2
        screen_center_y_1 = self.height / 32
        if screen_center_x_1 < 0:
            screen_center_x_1 = 0
        self.camera.move_to((screen_center_x_1, screen_center_y_1))

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x += 4
        if symbol == arcade.key.D:
            self.player.change_x += 4
        if symbol == arcade.key.LEFT:
            self.player.change_x -= 4
        if symbol == arcade.key.A:
            self.player.change_x -= 4
        if symbol == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 20
        if symbol == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player.change_y = 20

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 0
        if symbol == arcade.key.D:
            self.player.change_x = 0
        if symbol == arcade.key.LEFT:
            self.player.change_x = 0
        if symbol == arcade.key.A:
            self.player.change_x = 0
        if symbol == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 0
        if symbol == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player.change_y = 0


window = MyWindow()
arcade.run()
