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
                self.inventory.extend(["Dented Greatshield", "Training sword"])
            case "runeweaver":
                self.stats["int"] += 5
                self.stats["dex"] += 3
                self.inventory.extend(["Cracked Focus Crystal", "Runic Parchment"])
            case "apothecary":
                self.stats["int"] += 5
                self.stats["dex"] += 3
                self.stats["lck"] += 2
                self.inventory.extend(["Herbalistic Kit", "Glass Breaker"])
            case "silent_step":
                self.stats["dex"] += 5
                self.stats["per"] += 3
                self.stats["lck"] += 3
                self.inventory.extend(["Twin Daggers", "Lockpick Set"])
            case "spellblade":
                self.stats["str"] += 5
                self.stats["int"] += 3
                self.inventory.extend(["Infused Rapider", "Whetsotne"])
    
    def show_stats(self):
        inv_str = ", ".join(self.inventory)
        print(f"""
========================================
CHARACTER RECORD: {self.name.upper()}
========================================
 CLASS: {self.char_class.capitalize()}
 LEVEL: {self.level}        XP: {self.xp}
 HP:    {self.current_hp}/{self.max_hp}
 MANA:  {self.current_mana}/{self.max_mana}
----------------------------------------
 STR: {self.stats['str']}\t INT: {self.stats['int']}
 DEX: {self.stats['dex']}\t PER: {self.stats['per']}
 CON: {self.stats['con']}\t LCK: {self.stats['lck']}
----------------------------------------
 INVENTORY: {inv_str}
========================================
              """)
        
    def scan_room(self, room_data):
        print(f"Well well, it appears like {self.name} wants to scan the room, what secrets will we unveil?")
        modifier = (self.stats["int"] - 10) // 2
        roll = random.randint(1, 20)
        total = roll + modifier

        print(f"\n--- You rolled a {roll} (Total: {total}) ---")

        if roll == 20:
            print("--- CRITICAL SUCCESS! ---")
            print(f"Your mind is in sync with the arcane. {room_data['secret_info']}")
            return True
        elif total >= room_data["dc"]:
            print(f"Success! You notice something interesnting, what a keen eye... {room_data['secret_info']}")
            return True
        elif roll == 1:
            print("\n--- CRITICAL FAIL! ---")
            print(f"The arcane seems to be bothered by your mee existence...")
            #I still need to decide which effects does the critical fail will have...