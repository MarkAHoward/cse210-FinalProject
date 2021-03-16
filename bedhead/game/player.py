import arcade
from game import constants


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.CHARACTER_IMAGE, constants.CHARACTER_SCALING)
        self.center_x = int(constants.SCREEN_WIDTH / 5)
        self.center_y = int(constants.SCREEN_HEIGHT / 5)