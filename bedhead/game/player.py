import arcade
from game import constants


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = int(constants.SCREEN_WIDTH - 350)
        self.center_y = int(constants.SCREEN_HEIGHT - 375)
        self.change_x = 0
        self.change_y = 0
        self.alive = True
        self.scale = constants.CHARACTER_SCALING
        self.main_path = "cse210-FinalProject/bedhead/assets/Individual_Sprites/adventurer"
        self.idle_texture_pair = arcade.load_texture_pair(f"{self.main_path}-idle-00.png")
        self.jump_texture_pair = arcade.load_texture_pair(f"{self.main_path}-jump-02.png")
        self.fall_texture_pair = arcade.load_texture_pair(f"{self.main_path}-fall-01.png")

        # Set the initial texture
        self.texture = self.idle_texture_pair[0]

        # Hit box will be set based on the first image used.
        self.hit_box = self.texture.hit_box_points

        # Default to face-right
        self.character_face_direction = constants.RIGHT_FACING

        # Index of our current texture
        self.cur_texture = 0

        # How far have we traveled horizontally since changing the texture
        self.x_odometer = 0

        self.idle_textures = []
        for i in range(3):
            texture = arcade.load_texture_pair(f"{self.main_path}-idle-0{i}.png")
            self.idle_textures.append(texture)

        self.walk_textures = []
        for i in range(6):
            texture = arcade.load_texture_pair(f"{self.main_path}-run-0{i}.png")
            self.walk_textures.append(texture)

    def die(self):
        self.alive = False

    def reset_player(self):
        self.center_x = int(constants.SCREEN_WIDTH - 100)
        self.center_y = int(constants.SCREEN_HEIGHT / 2)
        self.change_x = 0
        self.change_y = 0
        self.alive = True

    def pymunk_moved(self, physics_engine, dx, dy, d_angle):
        """ Handle being moved by the pymunk engine """
        # Figure out if we need to face left or right
        if dx < -constants.DEAD_ZONE and self.character_face_direction == constants.RIGHT_FACING:
            self.character_face_direction = constants.LEFT_FACING
        elif dx > constants.DEAD_ZONE and self.character_face_direction == constants.LEFT_FACING:
            self.character_face_direction = constants.RIGHT_FACING

        # Are we on the ground?
        is_on_ground = physics_engine.is_on_ground(self)

        # Add to the odometer how far we've moved
        self.x_odometer += dx

        # Jumping animation
        if not is_on_ground:
            if dy > constants.DEAD_ZONE:
                self.texture = self.jump_texture_pair[self.character_face_direction]
                return
            elif dy < -constants.DEAD_ZONE:
                self.texture = self.fall_texture_pair[self.character_face_direction]
                return

        # Idle animation
        if abs(dx) <= constants.DEAD_ZONE:
            self.cur_texture += 1
            if self.cur_texture > 2:
                self.cur_texture = 0
            self.texture = self.idle_textures[self.cur_texture][self.character_face_direction]

        # Have we moved far enough to change the texture?
        if abs(self.x_odometer) > constants.DISTANCE_TO_CHANGE_TEXTURE:

            # Reset the odometer
            self.x_odometer = 0

            # Advance the walking animation
            self.cur_texture += 1
            if self.cur_texture > 5:
                self.cur_texture = 0
            self.texture = self.walk_textures[self.cur_texture][self.character_face_direction]