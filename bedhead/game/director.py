import arcade
from game import constants
from game.game_state import GameState

class Director(arcade.View):
    def __init__(self, views):
        """ This will start the game
        """
        super().__init__()

        self.views = views

        self._cast = None
        self._script = None
        self._controls = None
        self._input_service = None
        self._game_over = None

    def setup(self, game_state):
        """ This will setup the background color
        """
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self._cast = game_state.cast
        self._script = game_state.script
        self._input_service = game_state.input_service
        self._gravity_engine = game_state.gravity_engine
        self._game_over = game_state.game_over


    def on_update(self, delta_time):
        self._cue_action("update")
        self._gravity_engine.physics_engine.step()
        player = self._cast["player"][0]
        if player.alive == False:
            self.views['window'].show_view(self.views['game_over'])

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