import arcade
from game import constants

class Coins:
    def __init__(self, my_map):
        self.coin_list = arcade.SpriteList()
        self.coin_list = arcade.tilemap.process_layer(my_map, "Coins", constants.TILE_SCALING)

    def get_coins(self):
        return self.coin_list