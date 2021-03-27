import arcade

from game.player import Player
from game.mapmaker import MapMaker
from game.do_updates_action import DoUpdatesAction
from game.draw_actors_action import DrawActorsAction
from game.output_services import OutputServices
from game.do_collisions_action import DoCollisionsAction
from game.input_services import InputServices
from game.control_actors_action import ControlActorsAction
from game.do_collisions_action import DoCollisionsAction
from game.score import Score 
from game.gravity import Gravity
from game.screen_scroll_action import ScreenScrollAction
from game.items import Items
from game.game_over import GameOverView
from game.background_maker import BackgroundMaker

class GameState:

    def __init__(self):
        # self.game_over = GameOverView()

        self.cast = {}

        player = Player()
        self.cast['player'] = [player]

        items = Items()
        self.cast['items'] = [items]

        background = BackgroundMaker(self.cast)
        maps = MapMaker(self.cast)

        score = Score()
        self.cast["score"] = [score]
        
        self.script = {}

        self.output_services = OutputServices()
        self.input_service = InputServices(self.cast)
        self.gravity_engine = Gravity(self.cast)

        handle_collisions = DoCollisionsAction(self.cast)
        screen_scrolling = ScreenScrollAction()

        control_actors = ControlActorsAction(self.input_service, self.gravity_engine)
        do_outputs = DrawActorsAction(self.output_services, screen_scrolling)
        do_updates = DoUpdatesAction(self.gravity_engine)

        self.script["input"] = [control_actors]
        self.script["update"] = [do_updates, handle_collisions, screen_scrolling] # dont forget to add handle_collision_aciton after finishing code for it
        self.script["output"] = [do_outputs] 
