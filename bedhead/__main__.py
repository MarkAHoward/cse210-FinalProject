import arcade

from game.player import Player
from game.map import Map 
from game.decorations import Decorations 
from game.hazards import Hazards 
from game.walls import Walls 
from game.coins import Coins 
from game.keys import Keys
from game.background import Background 
from game.do_updates import Do_Updates 
from game.do_outputs import Do_Outputs 
from game.do_collisions import Do_Collisions 
from game.controls import Controls 
from game.score import Score 
from game.points import Points 
from game.items import Items 
from game.director import Director
from game.draw import Draw


def main():
    cast = {}

    walls = Walls()
    cast['walls'] = [walls]

    hazards = Hazards()
    cast['hazards'] = [hazards]

    coins = Coins()
    cast['coins'] = [coins]

    keys = Keys()
    cast['keys'] = [keys]

    background = Background()
    cast['background'] = [background]

    decorations = Decorations()
    cast['decorations'] = [decorations]

    player = Player()
    cast['player'] = [player]


    script = {}

    input_service = Controls()
    out_service = Do_Outputs()
    updates = Do_Updates()

    handle_collisions = Do_Collisions()

    script["input"] = [input_service]
    script["update"] = [updates, handle_collisions]
    script["output"] = [out_service] 

    bedhead = Director(cast, script, input_service)
    bedhead.setup()
    bedhead.on_draw
    arcade.run()
        '''
    def gernerate_map_list(self):
        my_level = Map()
        map_list = my_level.get_map()
        return map_list
        '''

if __name__ == "__main__":
    main()