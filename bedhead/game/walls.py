import arcade
from game import constants

class Walls:
    def __init__(self, my_map):
        self.wall_list = arcade.SpriteList()
        self.wall_list = arcade.tilemap.process_layer(my_map, "Walls", constants.TILE_SCALING)
        
    def get_walls(self):
        return self.wall_list