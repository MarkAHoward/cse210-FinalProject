import arcade
from game import constants


class Gravity:
    def __init__(self, cast):
        self.player_sprite = cast['player'][0]
        # self.wall_list = cast["walls"]
        # Set the gravity. (0, 0) is good for outer space and top-down.
        self.movement_value = 0
        self.jump_value = 0
        gravity = (0, -constants.GRAVITY)
        damping = constants.DEFAULT_DAMPING

        # Create the physics engine
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping,
                                                         gravity=gravity)
        
        self.physics_engine.add_sprite(self.player_sprite,
                                       friction=constants.PLAYER_FRICTION,
                                       mass=constants.PLAYER_MASS,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player",
                                       max_horizontal_velocity=constants.PLAYER_MAX_HORIZONTAL_SPEED,
                                       max_vertical_velocity=constants.PLAYER_MAX_VERTICAL_SPEED)

        self.physics_engine.add_sprite_list(cast['walls'],
                                            friction=constants.WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)
        self.physics_engine.add_sprite_list(cast['invisible'],
                                            friction=constants.WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)
                                            
        self.is_on_ground = self.physics_engine.is_on_ground(self.player_sprite)

    def _move_horizontally(self):
        # Update player forces based on keys pressed
        if self.movement_value > 0:
            # Create a force to the left. Apply it.
            if self.is_on_ground:
                force = (constants.PLAYER_MOVE_FORCE_ON_GROUND, 0)
            else:
                force = (constants.PLAYER_MOVE_FORCE_IN_AIR, 0)
            self.physics_engine.apply_force(self.player_sprite, force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(self.player_sprite, 0)
            self.physics_engine.step()
            
        elif self.movement_value < 0:
            # Create a force to the left. Apply it.
            if self.is_on_ground:
                force = (-constants.PLAYER_MOVE_FORCE_ON_GROUND, 0)
            else:
                force = (-constants.PLAYER_MOVE_FORCE_IN_AIR, 0)

            self.physics_engine.apply_force(self.player_sprite, force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(self.player_sprite, 0)
            self.physics_engine.step()
        else:
            # Player's feet are not moving. Therefore up the friction so we stop.
            self.physics_engine.set_friction(self.player_sprite, 1.0)
            self.physics_engine.step()

    def _jump_player(self):
        # find out if player is standing on ground
        if self.jump_value > 0:
            if self.physics_engine.is_on_ground(self.player_sprite):
                # She is! Go ahead and jump
                impulse = (0, constants.PLAYER_JUMP_IMPULSE)
                self.physics_engine.apply_impulse(self.player_sprite, impulse)
                # self.physics_engine.step()
            
    def set_movement_values(self, x, y):
        self.movement_value = x
        self.jump_value = y
    
    def move_player(self):
        self._move_horizontally()
        self._jump_player()
        self.physics_engine.step()


