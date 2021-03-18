import arcade

from game.decorations import Decorations 
from game.hazards import Hazards 
from game.walls import Walls 
from game.coins import Coins 
from game.keys import Keys
from game.background import Background 
from game import constants



class Map:
    def __init__(self):

        self.level = 1

        map_name = f"cse210-FinalProject/level_{self.level}.tmx"
        
        self.my_map = arcade.tilemap.read_tmx(map_name)

        background = Background(self.my_map)
        walls = Walls(self.my_map)
        hazards = Hazards(self.my_map)
        coins = Coins(self.my_map)
        keys = Keys(self.my_map)
        decorations = Decorations(self.my_map)

        self.map_list = []

        self.map_list.append(background.get_background())
        self.map_list.append(walls.get_walls())
        self.map_list.append(hazards.get_hazards())
        self.map_list.append(coins.get_coins())
        self.map_list.append(keys.get_keys())
        self.map_list.append(decorations.get_decorations())

    # def get_map(self):
    #     return self.map_list

