import arcade


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.player = arcade.Sprite(":resources:images/space_shooter/playerShip2_orange.png", 20)
        self.player.center_y = 500
        self.player.left = 10
        self.angle = 90