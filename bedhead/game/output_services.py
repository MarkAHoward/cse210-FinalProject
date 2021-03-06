import arcade


class OutputServices:

    def __init__(self):
        pass

    def start_screen(self):
        arcade.start_render()

    def draw_actor(self, actor):
        actor.draw()

    def draw_actors(self, actors):
        for actor in actors:
            self.draw_actor(actor)

    def write_score(self, text, view_left, view_bottom):
        arcade.draw_text(text, 10 + view_left, 10 + view_bottom,
                         arcade.csscolor.WHITE, 18)