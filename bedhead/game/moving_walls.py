import arcade


class Moving_Walls:
    def __init__(self, my_map):
        self.moving_wall_list = arcade.tilemap.process_layer(my_map, "Moving", TILE_SCALING)
    
    def get_moving_walls(self):
        return self.moving_wall_list
