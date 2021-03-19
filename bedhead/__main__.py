import arcade
from game.game_state import GameState
from game.director import Director

def main():
    
    bedhead = Director()
    game_state = GameState()
    bedhead.setup(game_state)
    arcade.run()
    
if __name__ == "__main__":
    main()
    arcade.run()