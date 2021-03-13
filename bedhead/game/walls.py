import arcade


class Walls:
    def __init__(self, my_map):
        self.wall_list = arcade.tilemap.process_layer(my_map, "Walls", TILE_SCALING)
    
    def get_coins(self):
        return self.wall_list
