from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service, gravity_engine):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self._gravity_engine = gravity_engine

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        x = self._input_service.get_x_movement()
        y = self._input_service.get_y_movement()
        player = cast["player"][0]
        player.change_x = x
        # if self._gravity_engine.#can_jump
        player.change_y = y
