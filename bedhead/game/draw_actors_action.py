from game.action import Action
from game import constants
import arcade


class DrawActorsAction(Action):

    def __init__(self, output_service, screen_scrolling):
        self._output_service = output_service
        self._screen_scrolling = screen_scrolling
    def execute(self, cast):
        self._output_service.start_screen()

        for group in cast['background']:
            for actor in group:
                self._output_service.draw_actor(actor)

        for group in cast:
            if group != "score" and group != "items" and group != "player" and group != "background" and group != "decorations":
                for actor in cast[group]:
                    self._output_service.draw_actor(actor)
            # else:
            #     if group == "score":
            #         Score = cast[group][0]
            #         self._output_service.write_score(Score.get_score_text() , self._screen_scrolling.view_left, self._screen_scrolling.view_bottom )
        self._output_service.draw_actor(cast["player"][0])
        self._output_service.draw_actors(cast["decorations"])
        Score = cast[group][0]
        self._output_service.write_score(Score.get_score_text() , self._screen_scrolling.view_left, self._screen_scrolling.view_bottom )

        
        
