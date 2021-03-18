import arcade
from game import constants

class Director(arcade.Window):
    def __init__(self):
        """ This will start the game
        """
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        self._cast = None
        self._script = None
        self._controls = None
        self._input_service = None

    def setup(self, game_state):
        """ This will setup the background color
        """
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self._cast = game_state.cast
        self._script = game_state.script
        self._input_service = game_state.input_service

    def on_update(self, delta_time):
        self._cue_action("update")

    def on_draw(self):
        self._cue_action("output")

    def on_key_press(self, symbol, modifiers):
        self._input_service.on_key_press(symbol, modifiers)
        self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.on_key_release(symbol, modifiers)
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)