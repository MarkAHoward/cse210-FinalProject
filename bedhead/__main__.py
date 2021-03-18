import arcade
from game.game_state import GameState
from game.director import Director

def main():
    # cast = {}
    # map_list = generate_map_list()
    # cast['map'] = [map_list]
    # draw = Draw(cast)

    # walls = Walls()
    # cast['walls'] = [walls]

    # hazards = Hazards()
    # cast['hazards'] = [hazards]

    # coins = Coins()
    # cast['coins'] = [coins]

    # keys = Keys()
    # cast['keys'] = [keys]

    # background = Background()
    # cast['background'] = [background]

    # decorations = Decorations()
    # cast['decorations'] = [decorations]
    
    # player = Player()
    # cast['player'] = [player]


    # script = {}

    # output_services = OutputServices()
    # input_service = InputControls()

    # control_actors = ControlActors(input_service)
    # do_outputs = DrawActors(output_services)
    # updates = Do_Updates()

    # handle_collisions = Do_Collisions()

    # script["input"] = [control_actors]
    # script["update"] = [updates]
    # script["output"] = [do_outputs] 

    bedhead = Director()
    game_state = GameState()
    bedhead.setup(game_state)
    arcade.run()

# def generate_map_list():
#     my_level = Map()
#     map_list = my_level.get_map()
#     return map_list
    

if __name__ == "__main__":
    main()
    arcade.run()