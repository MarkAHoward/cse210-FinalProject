import arcade
from game import constants

class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self, views):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("cse210-FinalProject/bedhead/assets/images/game_over.png")
        self.views = views

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        self.views['window'].show_view(self.views['start_screen'])
        # issues with getting the director and game_state to run from here, you cant 
        # import them without having an endless loop or have them as parameters because it doesnt work
        # so there is no way to retrieve there data