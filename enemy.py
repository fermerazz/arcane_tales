import random

class Enemy:
    def __init__(self, name, hp, attack_power, xp_reward):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attack_power = attack_power
        self.xp_reward = xp_reward

    def is_alive(self):
        return self.current_hp > 0