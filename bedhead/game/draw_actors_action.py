from game.action import Action
from game import constants
import arcade


class DrawActorsAction(Action):

    def __init__(self, output_service, screen_scrolling):
        self._output_service = output_service
        self._screen_scrolling = screen_scrolling
    def execute(self, cast):
        self._output_service.start_screen()


        map_list = []
        for group in cast:
            if group != "score" and group != "items":
                map_list.append(cast[group])
                for actor in map_list:
                    self._output_service.draw_actors(actor)
            else:
                if group == "score":
                    Score = cast[group][0]
                    self._output_service.write_score(Score.get_score_text() , self._screen_scrolling.view_left, self._screen_scrolling.view_bottom )
