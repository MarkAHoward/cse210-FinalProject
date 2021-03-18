from game.action import Action
from game import constants
from game.score import Score
import arcade


class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        self._output_service.start_screen()

        player = cast['player'][0]
        self._output_service.draw_actor(player)

        map_list = cast['map_list']
        for actors in map_list:
            actors = arcade.SpriteList()
            self._output_service.draw_actors(actors)

        score_text = f"Score: {Score.score_get()}"
        self._output_service.write_score(score_text)
