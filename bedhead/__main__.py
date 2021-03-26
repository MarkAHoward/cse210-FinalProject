import arcade
from game.game_state import GameState
from game.director import Director
from startup.start_screen import StartScreen
from startup.controls_screen import ControlScreen
from game.game_over import GameOverView
from game import constants

def main():

    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

    views = {}

    game = Director(views)
    game_state = GameState()
    start_screen = StartScreen(views)
    controls = ControlScreen(views)
    game_over = GameOverView(views)
    
    views['window'] = window
    views['game'] = game
    views['start_screen'] = start_screen
    views['controls'] = controls
    views['game_over'] = game_over
    views['game_state'] = game_state

    views['window'].show_view(views['start_screen'])
    game_view = views['start_screen']
    game_view.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()
    arcade.run()