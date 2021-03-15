import arcade
from game.draw import Draw

class Director(arcade.Window):
    def __init__(self, cast, script, controls):
        """ This will start the game
        """
        super().__init__(1000, 1000, "Bedhead")

        self._cast = cast
        self._script = script
        self._controls = controls

    def setup(self):
        """ This will setup the background color
        """
        arcade.set_background_color(arcade.color.ANTI_FLASH_WHITE)

    def on_draw(self):
        arcade.start_render()
        player = self._cast['player'][0]
        player.draw