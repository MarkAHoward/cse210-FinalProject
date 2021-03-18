import arcade

from game.player import Player
# from game.map import Map 
from game.do_updates_action import DoUpdatesAction
from game.draw_actors_action import DrawActorsAction
from game.output_services import OutputServices
from game.do_collisions_action import DoCollisionsAction
from game.input_services import InputServices
from game.control_actors_action import ControlActorsAction
from game.do_collisions_action import DoCollisionsAction
from game.score import Score 

class GameState:

    def __init__(self):
        
        self.cast = {}
        player = Player()
        self.cast['player'] = [player]
        self.script = {}

        self.output_services = OutputServices()
        self.input_service = InputServices()

        control_actors = ControlActorsAction(self.input_service)
        do_outputs = DrawActorsAction(self.output_services)
        updates = DoUpdatesAction()

        self.script["input"] = [control_actors]
        self.script["update"] = [updates]
        self.script["output"] = [do_outputs] 
