import arcade
from game import constants
from game.musichandler import MusicHandler


class Director(arcade.View):
    def __init__(self, views):
        """ This will start the game
        """
        super().__init__()

        self.BACKGROUND_MUSIC = ["cse210-FinalProject/bedhead/assets/Our-Mountain_v003_Looping.mp3",
                                 "cse210-FinalProject/bedhead/assets/Our-Mountain_v003_Looping.mp3"]

        self.views = views

        self._cast = None
        self._script = None
        self._controls = None
        self._input_service = None
        self._game_state = None

        self.musichander = MusicHandler()

    def setup(self, game_state):
        """ This will setup the background color
        """

        self._cast = game_state.cast
        self._script = game_state.script
        self._input_service = game_state.input_service
        self._gravity_engine = game_state.gravity_engine
        self._game_state = game_state

        # self.musichander.add_song_list(self.BACKGROUND_MUSIC)
        # self.musichander.play_song_looped()

    def on_update(self, delta_time):
        self._cue_action("update")
        self._gravity_engine.physics_engine.step()
        player = self._cast["player"][0]
        if player.alive == False:
            self._game_state.reset_game()
            self.views['game_over'].setup()
            self.views['window'].show_view(self.views['game_over'])
            # self.musichander.clear_queue()

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
