from game.action import Action
from game import constants
import arcade

class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        self._output_service.start_screen()

        map_list = []
        for group in cast:
            map_list.append(cast[group])
            for actor in map_list:
                self._output_service.draw_actors(actor)
