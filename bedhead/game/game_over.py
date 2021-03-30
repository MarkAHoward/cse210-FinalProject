import arcade
from game import constants


class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self, views):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("cse210-FinalProject/bedhead/assets/images/game_over.png")
        self.views = views

        # sound
        self.end_sound = arcade.load_sound(":resources:sounds/gameover2.wav")

    def setup(self):
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1,
                            0, constants.SCREEN_HEIGHT - 1)
        arcade.play_sound(self.end_sound)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        self.views['start_screen'].setup()
        self.views['window'].show_view(self.views['start_screen'])
