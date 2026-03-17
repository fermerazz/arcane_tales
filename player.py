import random 

class Player:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.xp = 0
        self.stats = {
            "str": 0, "dex": 0, "con": 0,
            "int": 0, "per": 0, "lck": 0
        }
        self.generat_stats()

        def generate_stats(self):
            pass