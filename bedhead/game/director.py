import arcade
from game.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

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
        arcade.set_background_color(arcade.color.SKY_BLUE)
        

    def on_draw(self):
        self._cue_action("output")

    # def on_key_press(self, symbol, modifiers):
    #     self._input_service.set_key(symbol, modifiers)
    #     self._cue_action("input")

    # def on_key_release(self, symbol, modifiers):
    #     self._input_service.remove_key(symbol, modifiers)
    #     self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)