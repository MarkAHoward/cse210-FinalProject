import arcade
from game.game_state import GameState
from game.director import Director
from game import constants

def main():

    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    game_view = Director()
    window.show_view(game_view)
    game_state = GameState()
    game_view.setup(game_state)
    arcade.run()
    
if __name__ == "__main__":
    main()
    arcade.run()