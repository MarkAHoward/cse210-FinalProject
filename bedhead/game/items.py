import arcade

class Items:
    def __init__(self):
        self.keys_recieved = 0
        self.next_level = False
        self.win_screen = False

    def add_key_to_inventory(self):
        self.keys_recieved += 1

    def go_to_next_level(self):
        self.next_level = True

    def win_screen_activate(self):
        self.win_screen = True
    
    def level_two_keys(self):
        self.keys_recieved += 2

