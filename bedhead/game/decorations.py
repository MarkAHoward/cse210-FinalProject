
class Decorations:
    def __init__(self, my_map):
        self.decoration_list = arcade.SpriteList()
        self.decoration_list = arcade.tilemap.process_layer(my_map, "Decorations", constants.TILE_SCALING)

    def get_decorations(self):