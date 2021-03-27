import arcade
from game import constants


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.CHARACTER_IMAGE, constants.CHARACTER_SCALING)
        self.center_x = int(constants.SCREEN_WIDTH / 2)
        self.center_y = int(constants.SCREEN_HEIGHT / 2)
        self.change_x = 0
        self.change_y = 0
        self.alive = True

    def die(self):
        self.alive = False
