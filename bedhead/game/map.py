import arcade

from game import constants
from game.decorations import Decorations 
from game.hazards import Hazards 
from game.walls import Walls 
from game.coins import Coins 
from game.keys import Keys
from game.background import Background 
from game.moving_walls import Moving_Walls


class Map:
    def __init__(self):

        self.level = 1
        
        my_map = self.load_map(self.level)

        self.end_of_map = my_map.map_size.width * constants.GRID_PIXEL_SIZE

        self.map_list = []

        background = Background(my_map)
        walls = Walls(my_map)
        hazards = Hazards(my_map)
        coins = Coins(my_map)
        keys = Keys(my_map)
        decorations = Decorations(my_map)
        moving = Moving_Walls(my_map)

        self.map_list.append(background.get_background())
        self.map_list.append(walls.get_walls())
        self.map_list.append(moving.get_moving_walls())
        self.map_list.append(hazards.get_hazards())
        self.map_list.append(coins.get_coins())
        self.map_list.append(keys.get_keys())
        self.map_list.append(decorations.get_decorations())
    
    def get_map(self):
        return self.map_list
    
    def load_map(self, level):
        map_name = f"level_{level}.tmx"
        my_map = arcade.tilemap.read_tmx(map_name)
        return my_map
