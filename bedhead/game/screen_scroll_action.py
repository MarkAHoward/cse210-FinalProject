from game import constants
from game.action import Action
import arcade

class ScreenScrollAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """
    def __init__(self):
        self.view_bottom = 0
        self.view_left = 0
        self._changed = False

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        player_sprite = cast["player"][0]
        self.move_screen(player_sprite)

    def _scroll_left(self, player_sprite):
        # Scroll left
        left_boundary = self.view_left + constants.LEFT_VIEWPORT_MARGIN
        if player_sprite.left < left_boundary:
            self.view_left -= left_boundary - player_sprite.left
            self._changed = True

    def _scroll_right(self, player_sprite):
        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_VIEWPORT_MARGIN
        if player_sprite.right > right_boundary:
            self.view_left += player_sprite.right - right_boundary
            self._changed = True

    def _scroll_up(self, player_sprite):
        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.TOP_VIEWPORT_MARGIN
        if player_sprite.top > top_boundary:
            self.view_bottom += player_sprite.top - top_boundary
            self._changed = True

    def _scroll_down(self, player_sprite):
        # Scroll down
        bottom_boundary = self.view_bottom + constants.BOTTOM_VIEWPORT_MARGIN
        if player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - player_sprite.bottom
            self._changed = True

    def move_screen(self, player_sprite):
        self._scroll_left(player_sprite)
        self._scroll_right(player_sprite)
        self._scroll_down(player_sprite)
        self._scroll_up(player_sprite)
        if self._changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)