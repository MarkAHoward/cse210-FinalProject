import arcade
from game import constants

class Hazards:
    def __init__(self, my_map):
        self.hazard_list = arcade.SpriteList()
        self.hazard_list = arcade.tilemap.process_layer(my_map, "Hazards", constants.TILE_SCALING)
    
    def get_hazards(self):
        return self.hazard_list