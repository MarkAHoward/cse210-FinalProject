import arcade

from game.decorations import Decorations 
from game.hazards import Hazards 
from game.walls import Walls 
from game.coins import Coins 
from game.keys import Keys
from game.background import Background 
from game import constants



class Map(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        self.level = 1

        map_name = f"level_{self.level}.tmx"

        my_map = arcade.tilemap.read_tmx(map_name)

        background = Background(my_map)
        walls = Walls(my_map)
        hazards = Hazards(my_map)
        coins = Coins(my_map)
        keys = Keys(my_map)
        decorations = Decorations(my_map)

        self.map_list = []

        self.map_list.append(background.get_background())
        self.map_list.append(walls.get_walls())
        self.map_list.append(hazards.get_hazards())
        self.map_list.append(coins.get_coins())
        self.map_list.append(keys.get_keys())
        self.map_list.append(decorations.get_decorations())

        for k in self.map_list:
            k.draw()

    def get_map(self):
        return self.map_list

