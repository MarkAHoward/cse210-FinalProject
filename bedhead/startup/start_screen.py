import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Bedhead"

class StartScreen(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.button_list_1 = None
        self.button_list_2 = None
        self.highlight_list = None

        self.highlight = None

        self.button_1 = None
        self.button_2 = None
        self.button_3 = None

        arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

    def setup(self):
        self.button_list_1 = arcade.SpriteList()
        self.button_list_2 = arcade.SpriteList()

        self.highlight_list = arcade.SpriteList()

        image_source_1 = "cse210-FinalProject/bedhead/assets/start_game_button.png"
        image_source_2 = "cse210-FinalProject/bedhead/assets/controls_button.png"
        image_source_3 = None
        image_source_4 = "cse210-FinalProject/bedhead/assets/highlight_box.png"

        self.button_1 = arcade.Sprite(image_source_1)
        self.button_1.center_x = SCREEN_WIDTH / 2
        self.button_1.center_y = SCREEN_HEIGHT * (2/3)
        
        self.button_2 = arcade.Sprite(image_source_2)
        self.button_2.center_x = SCREEN_WIDTH / 2
        self.button_2.center_y = SCREEN_HEIGHT * (1/3)

        # self.button_3 = arcade.Sprite(image_source_3)
        # self.button_3.center_x = SCREEN_WIDTH - 100
        # self.button_3.center_y = 50

        self.button_list_1.append(self.button_1)
        self.button_list_1.append(self.button_2)
        # self.button_list_2.append(self.button_3)

        self.highlight = arcade.Sprite(image_source_4)
        self.highlight.center_x = SCREEN_WIDTH / 2
        self.highlight.center_y = SCREEN_HEIGHT * (2/3)
        
        self.highlight_list.append(self.highlight)


    def on_draw(self):
        arcade.start_render()

        self.highlight_list.draw()

        self.button_list_1.draw()
        # self.button_list_2.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            if self.highlight.center_y == SCREEN_HEIGHT * (2/3):
                pass
            elif self.highlight.center_y == SCREEN_HEIGHT * (1/3):
                self.highlight.center_y = SCREEN_HEIGHT * (2/3)
        if key == arcade.key.S or key == arcade.key.DOWN:
            if self.highlight.center_y == SCREEN_HEIGHT * (2/3):
                self.highlight.center_y = SCREEN_HEIGHT * (1/3)
            elif self.highlight.center_y == SCREEN_HEIGHT * (1/3):
                pass
        if key == arcade.key.ENTER:
            self.change_screen()
    
    def on_update(self, delta_time):
        self.highlight.update()
    
    def change_screen(self):
        pass
    

def main():
    """ Main method """
    window = StartScreen()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
    arcade.run()



        
