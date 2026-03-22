#Here we have the information and basically the world building! If you happen to be reading this
#Feel free to modify this at your will

from enemy import Enemy

world_map = {
    "dungeon_entrance": {
        "description": "A cold stone archway carved into the mountainside. Moss clings to the damp walls.",
        "dc": 10,
        "secret_info": "You notice a faint, glowing blue rune hidden behind the moss. It hums with power.",
        "exits": {"north": "echoing_hall"}
    },
    "echoing_hall": {
        "description": "A vast corridor where every footstep rings out. Old banners hang tattered from the ceiling.",
        "dc": 12,
        "secret_info": "Tucked inside a rotted banner is a small silver key!",
        "exits": {"south": "dungeon_entrance", "east": "apothecary_lab", "west": "guard_barracks"}
    },
    "apothecary_lab": {
        "description": "The air is thick with the scent of dried herbs and sulfur. Shards of glass litter the floor.",
        "dc": 15,
        "secret_info": "Beneath a heavy iron mortar, you find a recipe for a 'Restorative Draught'.",
        "exits": {"west": "echoing_hall"}
    },
    "guard_barracks": {
        "description": "Overturned bunks and rusted armor plates suggest a struggle happened here long ago.",
        "dc": 8,
        "secret_info": "Inside a hollowed-out bedpost, someone hid a pouch of 10 gold coins!",
        "exits": {"east": "echoing_hall", "north": "sealed_vault"}
    },
    "sealed_vault": {
        "description": "A heavy iron door stands before you, etched with complex geometric patterns.",
        "dc": 18,
        "secret_info": "The patterns reveal a hidden sequence: 'Circle, Triangle, Square'. This must be the lock code!",
        "exits": {"south": "guard_barracks", "north": "throne_room"}
    },
        "throne_room": {
        "description": "A massive hall lit by purple torches. An ancient Lich sits upon a throne of bone.",
        "dc": 15,
        "secret_info": "The Lich's crown is cracked; a strike to the head might deal double damage!",
        "exits": {"south": "sealed_vault"},
        "boss": Enemy("The Bone Lich", 50, 12, 500) # Name, HP, Attack, XP
    }
}