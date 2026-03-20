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
        #We want to tie the hp to the con attribute
        self.max_hp = 50 + (self.stats["con"] * 5)
        self.current_hp = self.max_hp
        #we'll do the same here but for the mana with the int attribute
        self.max_mana = 20 + (self.stats["int"] * 8)
        self.current_mana = self.max_mana
        self.inventory = []
        self.generate_stats()

    def generate_stats(self):
        for stat in self.stats:
            self.stats[stat] = random.randint(3, 18)
            
        match self.char_class:
            case "vanguard":
                self.stats["str"] += 5
                self.stats["con"] += 3
                self.inventory.append("Dented Greatshield", "Training sword")
            case "runeweaver":
                self.stats["int"] += 5
                self.stats["dex"] += 3
                self.inventory.append("Cracked Focus Crystal", "Runic Parchment")
            case "apothecary":
                self.stats["int"] += 5
                self.stats["dex"] += 3
                self.stats["lck"] += 2
                self.inventory.append("Berbalistic Kit", "Glass Breaker")
            case "silent_step":
                self.stats["dex"] += 5
                self.stats["per"] += 3
                self.stats["lck"] += 3
                self.inventory.append("Twin Daggers", "Lockpick Set")
            case "spellblade":
                self.stats["str"] += 5
                self.stats["int"] += 3
                self.inventory.append("Infused Rapider", "Whetsotne")