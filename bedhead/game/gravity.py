import arcade
from game import constants


class Gravity:
    def __init__(self, cast):
        self.player_sprite = cast['player'][0]
        self.wall_list = cast["walls"]
        # Set the gravity. (0, 0) is good for outer space and top-down.
        gravity = (0, -constants.GRAVITY)

        # Create the physics engine
        self.physics_engine = arcade.PymunkPhysicsEngine(gravity=gravity)
        
        self.physics_engine.add_sprite(self.player_sprite,
                                       friction=constants.PLAYER_FRICTION,
                                       mass=constants.PLAYER_MASS,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player",
                                       max_horizontal_velocity=constants.PLAYER_MAX_HORIZONTAL_SPEED,
                                       max_vertical_velocity=constants.PLAYER_MAX_VERTICAL_SPEED)

        self.physics_engine.add_sprite_list(self.wall_list,
                                            friction=constants.WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

