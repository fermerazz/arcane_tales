import pygame
from menu import show_main_menu, show_character_creation, clear_screen
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
            clear_screen()
            hero.show_stats()
            input("Are you ready, Traveler? Press Enter to Begin...")
            
            #After this, we will create the playable loop! Here comes the fun...
            game_running = True
            current_location = ""

            while game_running:
                pass
            
        case "load":
            print("\nLoading ancient scrolls (Saved File)...")
        case "exit":
            print("\nFarewell, traveler. The realm awaits your return.")
            pygame.mixer.music.fadeout(2000)
            pygame.time.wait(2000)
            pygame.quit()

if __name__ == "__main__":
    main()
