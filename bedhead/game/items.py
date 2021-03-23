import arcade

class Items:
    def __init__(self):
        self.keys_recieved = 0

    def add_key_to_inventory(self):
        self.keys_recieved += 1
