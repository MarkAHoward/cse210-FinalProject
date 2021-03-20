import arcade
from game import constants

class InputServices:

    def __init__(self):
            self._x = 0
            self._y = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """ 
        if key == arcade.key.UP or key == arcade.key.W:
            self._y = constants.PLAYER_JUMP_SPEED
                # arcade.play_sound(self.jump_sound)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self._y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self._x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self._x = constants.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            self._y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self._y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self._x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self._x = 0

    def get_x_movement(self):
        return self._x

    def get_y_movement(self):
        return self._y

