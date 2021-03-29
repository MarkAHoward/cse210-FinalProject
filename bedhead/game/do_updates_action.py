from game import constants
from game.action import Action
import arcade

class DoUpdatesAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """
    def __init__(self, physics_engine):
        self.physics_engine = physics_engine

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        needs_update = []
        needs_update.append(cast['moving_walls'])
        needs_update.append(cast['hazards'])
        for group in needs_update:
            group.update()
            for item in group:
                if item.boundary_right and item.right > item.boundary_right and item.change_x > 0:
                    item.change_x *= -1
                if item.boundary_left and item.left < item.boundary_left and item.change_x < 0:
                    item.change_x *= -1
                if item.boundary_top and item.top > item.boundary_top and item.change_y > 0:
                    item.change_y *= -1
                if item.boundary_bottom and item.bottom < item.boundary_bottom and item.change_y < 0:
                    item.change_y *= -1
            # Mark could make this ^^^^^^^^^^^^^^^^ look better or like more object oriented or something
        self.physics_engine.move_player()
        self.physics_engine.physics_engine.step()

    
