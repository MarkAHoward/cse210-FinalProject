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
            self._output_service.draw_actor(group[0])
            self._output_service.draw_actor(group[1])
            for actor in group:
                if actor.center_x < cast["player"][0].center_x + 600 and actor.center_x > cast["player"][0].center_x - 600:               
                    self._output_service.draw_actor(actor)    
        for group in cast:
            if group != "score" and group != "items" and group != "player" and group != "background" and group != "decorations" and group != "invisible":
                for actor in cast[group]:
                    if actor.center_x < cast["player"][0].center_x + 600 and actor.center_x > cast["player"][0].center_x - 600:
                            self._output_service.draw_actor(actor)
                    
        self._output_service.draw_actor(cast["player"][0])

        for actor in cast['decorations']:
            if actor.center_x < cast["player"][0].center_x + 600 and actor.center_x > cast["player"][0].center_x - 600:
                self._output_service.draw_actor(actor)
        Score = cast[group][0]

        self._output_service.write_score(Score.get_score_text() , self._screen_scrolling.view_left, self._screen_scrolling.view_bottom )

        
        
