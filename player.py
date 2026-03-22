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
        self.roll_penalty = 0
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
        total = roll + modifier - self.roll_penalty

        if self.roll_penalty > 0:
            print(f"Your brain fog substracts {self.roll_penalty} from your effort...")
            self.roll_penalty = 0

        print(f"\n--- You rolled a {roll} (Total: {total}) ---")

        if roll == 20:
            print("--- CRITICAL SUCCESS! ---")
            print(f"Your mind is in sync with the arcane. {room_data['secret_info']}")
            return True
        
        elif roll == 1:
            print("\n--- CRITICAL FAIL! ---")
            print(f"The arcane seems to be bothered by your petty existence...")
            print("You feel a little lightheaded, your mana decreases by 10 pts!")
            self.current_mana = max(0, self.current_mana - 10)
            self.roll_penalty = 5
            return False
        
        elif total >= room_data["dc"]:
            print(f"Success! You notice something interesnting, what a keen eye... {room_data['secret_info']}")
            return True
        else:
            print("The shadows hide their secrets well. Your find nothing unusual.")
            return False
    
    def attack(self, target):
        str_mod = (self.stats["str"] - 10) // 2
        int_mod = (self.stats["int"] - 10) // 2

        if self.char_class == "spellblade":
            modifier = max(str_mod, int_mod)
            print(f"{self.name} channels arcane energy through their blade...")
        else:
            modifier = str_mod

        roll = random.randint(1, 20)
        total = roll + modifier

        print(f"{self.name} swings their weapon... (Roll: {roll} + {modifier} = {total})")
        if total >= 10:
            damage = random.randint(5, 15) + modifier
            
            if self.char_class == "spellblade" and self.current_mana >= 5:
                self.current_mana -= 5
                magical_bonus = int_mod
                damage += magical_bonus
                print(f"The blade glows purple! (+{magical_bonus} Magic Damage, -5 Mana)")
            elif self.char_class == "spellblade":
                print("Your mana is too low to infuse the blade!")

            target.current_hp -= damage
            print(f"HIT! You deal {damage} damage to {target.name}!")
            print(f"[{target.name} HP: {max(0, target.current_hp)}/{target.max_hp}]")
        else:
            print(f"MISS! Your strike whistles through the air.")