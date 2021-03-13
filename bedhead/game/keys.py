import arcade
from game import constants

class Keys:
    def __init__(self, my_map):
        self.key_list = arcade.SpriteList()
        self.key_list = arcade.tilemap.process_layer(my_map, "Keys", constants.TILE_SCALING)
    
    def get_keys(self):
        return self.key_list
