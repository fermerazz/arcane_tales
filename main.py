import pygame
from menu import show_main_menu, show_character_creation
from player import Player

def main():
    #initializing the mixer
    pygame.mixer.init()
    pygame.mixer.music.load("soundtrack.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1, fade_ms=3000)

    music_paused = False

    player_choice, music_paused = show_main_menu(music_paused)

    match player_choice:
        case "start":
            print("\nInitializing character creation...")
            name, char_class = show_character_creation()
            hero = Player(name, char_class)

            print(f"\n--- Hero Stats ---")
            print(f"Name: {hero.name} | Class: {hero.char_class.capitalize()}")
            print(f"HP: {hero.current_hp}/{hero.max_hp} | STR: {hero.stats["str"]}")
            print(f"Starting Gear: {hero.inventory}")
        case "load":
            print("\nLoading ancient scrolls (Saved File)...")
        case "exit":
            print("\nFarewell, traveler. The realm awaits your return.")
            pygame.mixer.music.fadeout(2000)
            pygame.time.wait(2000)
            pygame.quit()

if __name__ == "__main__":
    main()
