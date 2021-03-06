import arcade
from game import constants

class MapMaker:
    def __init__(self, cast, level_number):

        self.level = level_number

        map_name = f"cse210-FinalProject/level_{self.level}.tmx"
        
        self.my_map = arcade.tilemap.read_tmx(map_name)

        wall_list = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        wall_list = arcade.tilemap.process_layer(self.my_map, "Walls", constants.TILE_SCALING)

        moving_wall_list = arcade.SpriteList(use_spatial_hash=True)
        moving_wall_list = arcade.tilemap.process_layer(self.my_map, "Moving", constants.TILE_SCALING)

        hazard_list = arcade.SpriteList(use_spatial_hash=True)
        hazard_list = arcade.tilemap.process_layer(self.my_map, "Hazards", constants.TILE_SCALING)

        coin_list = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        coin_list = arcade.tilemap.process_layer(self.my_map, "Coins", constants.TILE_SCALING)

        key_list = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        key_list = arcade.tilemap.process_layer(self.my_map, "Keys", constants.TILE_SCALING)

        decoration_list = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        decoration_list = arcade.tilemap.process_layer(self.my_map, "Decorations", constants.TILE_SCALING)

        door_list = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        door_list = arcade.tilemap.process_layer(self.my_map, "Doors", constants.TILE_SCALING)

        invisible_list = arcade.SpriteList(use_spatial_hash=True, is_static=True)
        invisible_list = arcade.tilemap.process_layer(self.my_map, "Invisible", constants.TILE_SCALING)

        cast['walls'] = wall_list
        cast['moving_walls'] = moving_wall_list
        cast['hazards'] = hazard_list
        cast['coins'] = coin_list
        cast['keys'] = key_list
        cast['doors'] = door_list
        cast['decorations'] = decoration_list
        cast['invisible'] = invisible_list



