import arcade

class Items:
    def __init__(self):
        self.keys_recieved = 0
        self.next_level = False

    def add_key_to_inventory(self):
        self.keys_recieved += 1

    def go_to_next_level(self):
        self.next_level = True

