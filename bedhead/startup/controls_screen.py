import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Bedhead"

class ControlScreen(arcade.View):

    def __init__(self, views):

        super().__init__()

        self.views = views

        self.button_list = None
        self.highlight_list = None

        self.button_list = arcade.SpriteList()
        self.highlight_list = arcade.SpriteList()

        self.button = None

        arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

        image_source_1 = "cse210-FinalProject/bedhead/assets/back_button.png"

        self.button = arcade.Sprite(image_source_1)
        self.button.center_x = SCREEN_WIDTH - 150
        self.button.center_y = 50

        self.button_list.append(self.button)

    def on_draw(self):
        arcade.start_render()
        self.button_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.views['window'].show_view(self.views['start_screen'])
