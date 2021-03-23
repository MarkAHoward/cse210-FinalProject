import arcade
from game import constants

class StartScreen():

    def __init__(self, cast):

        cast['start_screen'] = True
        cast['opening'] = True
        cast['controls'] = False

        button_list_1 = None
        button_list_2 = None
        # highlight_list = None

        highlight = None

        button_1 = None
        button_2 = None
        button_3 = None

        button_list_1 = arcade.SpriteList()
        button_list_2 = arcade.SpriteList()

        # highlight_list = arcade.SpriteList()

        image_source_1 = "cse210-FinalProject/bedhead/assets/start_game_button.png"
        image_source_2 = "cse210-FinalProject/bedhead/assets/controls_button.png"
        image_source_3 = "cse210-FinalProject/bedhead/assets/back_button.png"
        image_source_4 = "cse210-FinalProject/bedhead/assets/highlight_box.png"

        button_1 = arcade.Sprite(image_source_1)
        button_1.center_x = constants.SCREEN_WIDTH / 2
        button_1.center_y = constants.SCREEN_HEIGHT * (2/3)
        
        button_2 = arcade.Sprite(image_source_2)
        button_2.center_x = constants.SCREEN_WIDTH / 2
        button_2.center_y = constants.SCREEN_HEIGHT * (1/3)

        button_3 = arcade.Sprite(image_source_3)
        button_3.center_x = constants.SCREEN_WIDTH - 150
        button_3.center_y = 50

        button_list_1.append(button_1)
        button_list_1.append(button_2)
        button_list_2.append(button_3)

        highlight = arcade.Sprite(image_source_4)
        highlight.center_x = constants.SCREEN_WIDTH / 2
        highlight.center_y = constants.SCREEN_HEIGHT * (2/3)

        # highlight_list.append(highlight)

        cast['highlight'] = highlight
        cast['button_list_1'] = button_list_1
        cast['button_list_2'] = button_list_2
        







        
