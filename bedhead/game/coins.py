import arcade
import constants

class Coins:
    def __init__(self, my_map):
        self.coin_list = arcade.tilemap.process_layer(my_map, "Coins", TILE_SCALING)
    
    def get_coins(self):
        return self.coin_list


