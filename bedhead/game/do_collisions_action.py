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

    def __init__(self, cast, game_state):
        self.player_sprite = cast['player'][0]
        self.coin_list = cast['coins']
        self.key_list = cast['keys']
        self.hazard_list = cast["hazards"]
        self.Score = cast["score"][0]
        self.items = cast["items"][0]
        self.door_list = cast['doors']
        self.game_state = game_state

        # coin sounds
        self.coin_collect = arcade.load_sound(":resources:sounds/coin2.wav")
        self.key_collect = arcade.load_sound(
            "cse210-FinalProject/bedhead/assets/mixkit-game-loot-win-2013.wav")

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self.on_coin_collision()
        self.on_key_collision()
        self.on_hazard_collision()
        self.on_door_collision()

    def on_coin_collision(self):
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.coin_list)
        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            self.Score.score += 5
            # sound
            arcade.play_sound(self.coin_collect)

    def on_key_collision(self):
        key_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.key_list)
        for key in key_hit_list:
            key.remove_from_sprite_lists()
            self.items.add_key_to_inventory()
            # sound
            arcade.play_sound(self.key_collect)

    def on_hazard_collision(self):
        hazards_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.hazard_list)
        for hazard in hazards_hit_list:
            self.player_sprite.die()

    def on_door_collision(self):
        door_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.door_list)
        for door in door_hit_list:
            if self.items.keys_recieved == 2:
                self.items.go_to_next_level()   
            elif self.items.keys_received == 3:
                self.items.win_screen()
