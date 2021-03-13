import arcade
from game import constants

class Background:
    def __init__(self, my_map):
        self.background_list = arcade.tilemap.process_layer(my_map, "Background", constants.TILE_SCALING)
    
    def get_background(self):
        return self.background_list
