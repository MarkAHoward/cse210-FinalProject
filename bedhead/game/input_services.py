import arcade
from game import constants

class InputServices:

    def __init__(self, cast):
            self._x = 0
            self._y = 0
            self.cast = cast

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """ 

        # I know this is a lot of code but if we want to condense it later somewhere else we can
        if self.cast['start_screen'] == True:
            if key == arcade.key.W or key == arcade.key.UP:
                if self.cast['controls'] == True:
                    self.cast['highlight'].center_y = 50
                    self.cast['highlight'].center_x = constants.SCREEN_WIDTH - 100
                if self.cast['opening'] == True:
                    if self.cast['highlight'].center_y == constants.SCREEN_HEIGHT * (2/3):
                        pass
                    elif self.cast['highlight'].center_y == constants.SCREEN_HEIGHT * (1/3):
                        self.cast['highlight'].center_y = constants.SCREEN_HEIGHT * (2/3)
            if key == arcade.key.S or key == arcade.key.DOWN:
                if self.cast['controls'] == True:
                    self.cast['highlight'].center_y = 50
                    self.cast['highlight'].center_x = constants.SCREEN_WIDTH - 100
                if self.cast['opening'] == True:
                    if self.cast['highlight'].center_y == constants.SCREEN_HEIGHT * (2/3):
                        self.cast['highlight'].center_y = constants.SCREEN_HEIGHT * (1/3)
                    elif self.cast['highlight'].center_y == constants.SCREEN_HEIGHT * (1/3):
                        pass
                    
            if key == arcade.key.ENTER:
                
                if self.cast['start_screen'] == True:
                    if self.cast['highlight'].center_y == constants.SCREEN_HEIGHT * (2/3):
                        self.cast['start_screen'] = False
                    else:
                        if self.cast['opening'] == True:
                            self.cast['opening'] = False
                            self.cast['controls'] = True
                            self.cast['highlight'].center_y = 50
                            self.cast['highlight'].center_x = constants.SCREEN_WIDTH - 150
                        elif self.cast['controls'] == True:
                            self.cast['opening'] = True
                            self.cast['controls'] = False
                            self.cast['highlight'].center_y = constants.SCREEN_HEIGHT * (1/3)
                            self.cast['highlight'].center_x = constants.SCREEN_WIDTH / 2

        # End of the Code for the start screen

        else:
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

