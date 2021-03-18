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
