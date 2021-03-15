import arcade
from game.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH
from game.draw import Draw

class Director(arcade.Window):
    def __init__(self, cast, script, controls):
        """ This will start the game
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self._cast = cast
        self._script = script
        self._controls = controls

    def setup(self):
        """ This will setup the background color
        """
        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        player = self._cast['player'][0]
        player.draw