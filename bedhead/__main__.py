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
from game.draw import Draw
# from game.output_services import OutputServices
from game.do_collisions import Do_Collisions 
# from game.input_controls import InputControls
from game.score import Score 
from game.points import Points 
from game.items import Items 
from game.director import Director


def main():
    cast = {}
    map_list = generate_map_list()
    # cast['map'] = [map_list]
    # draw = Draw(cast)
    '''
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

    draw = Draw(cast)
    
    player = Player()
    cast['player'] = [player]


    script = {}

    output_services = OutputServices()

    input_service = i()
    do_outputs = DrawActorsAction(output_services)
    updates = Do_Updates()

    handle_collisions = Do_Collisions()

    script["input"] = [input_service]
    script["update"] = [updates, handle_collisions]
    script["output"] = [do_outputs] 

    # bedhead = Director(cast, script, input_service)
    # bedhead.setup()
    # arcade.run()
    '''
def generate_map_list():
    my_level = Map()
    map_list = my_level.get_map()
    return map_list
    

if __name__ == "__main__":
    main()
    arcade.run()