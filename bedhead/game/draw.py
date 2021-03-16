import arcade

class Draw():
    def __init__(self, cast):
        arcade.start_render()
        for k in cast['map']:
            k = arcade.SpriteList()
            k.draw()

        # score_text = f"Score: {score}"
        # arcade.draw_text(score_text, 10 + view_left, 10 + view_bottom, arcade.csscolor.WHITE, 18)