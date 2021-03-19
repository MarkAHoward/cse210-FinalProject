from game.action import Action
from game import constants
import arcade

class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        self._output_service.start_screen()
        
        player = cast['player'][0]
        self._output_service.draw_actor(player)

        map_list = []
        map_list.append(cast['background'])
        map_list.append(cast['walls'])
        map_list.append(cast['moving_walls'])
        map_list.append(cast['hazards'])
        map_list.append(cast['coins'])
        map_list.append(cast['keys'])
        map_list.append(cast['decorations'])
        for actor in map_list:
            self._output_service.draw_actors(actor)


