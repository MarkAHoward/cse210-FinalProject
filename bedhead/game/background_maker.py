import arcade
from game import constants

class BackgroundMaker:
    def __init__(self, cast):

        self.level = 1

        map_name = f"cse210-FinalProject/level_{self.level}.tmx"
        
        self.my_map = arcade.tilemap.read_tmx(map_name)

        background_list = []

        background_list1 = arcade.SpriteList(is_static=True)
        background_list1 = arcade.tilemap.process_layer(self.my_map, "Background", constants.TILE_SCALING)

        background_list2 = arcade.SpriteList(is_static=True)
        background_list2 = arcade.tilemap.process_layer(self.my_map, "Background_Decorations", constants.TILE_SCALING)

        background_list.append(background_list1)
        background_list.append(background_list2)

        cast['background'] = background_list

