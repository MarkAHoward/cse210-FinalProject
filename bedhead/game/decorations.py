import arcade
from game import constants

class Decorations:
    def __init__(self, my_map):
        self.decoration_list = arcade.tilemap.process_layer(my_map, "Decorations", constants.TILE_SCALING)
    
    def get_decorations(self):
        return self.decoration_list