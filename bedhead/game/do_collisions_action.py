from game import constants
from game.action import Action
import arcade


class DoCollisionsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.

    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        player_sprite = cast['player'][0]
        coin_list = cast['coins']
        key_list = cast['keys']
        hazard_list = cast["hazards"]
        Score = cast["score"][0]

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(player_sprite, coin_list)
        key_hit_list = arcade.check_for_collision_with_list(player_sprite, key_list)
        hazards_hit_list = arcade.check_for_collision_with_list(player_sprite, hazard_list)

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            Score.score += 5
        
        for key in key_hit_list:
            key.remove_from_sprite_lists()
            # something to return the information that the key has been hit and stored in the key list that lets you go through a door
            
        for hazard in hazards_hit_list:
            return None # game over