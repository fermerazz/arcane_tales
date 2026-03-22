import pygame
from menu import show_main_menu, show_character_creation, clear_screen
from player import Player
from world import world_map

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
            current_location = "dungeon_entrance"

            while game_running:
                room = world_map[current_location]
                print(f"\n--- {current_location.replace('_',' ').upper()} ---")
                print(room["description"])

                if "boss" in room and room["boss"].is_alive():
                    print(f"A wild {room['boss'].name} blocks your path!")
                
                action = input("\n(Scan / Move / Stats / Attack / Exit) > ").lower().strip()
                if action == "scan":
                    hero.scan_room(room)
                elif action == "stats":
                    hero.show_stats()
                    input("Press enter to return...")
                elif action == "move":
                    direction = input("Which direction do you wish to go? (North/South/East/West) > ").lower().strip()
                    if direction in room["exits"]:
                        current_location = room["exits"][direction]
                        clear_screen()
                        print(f"You travel {direction}...")
                    else:
                        print("The path is blocked by a huge stone, believe me, nobody can move it...")
                elif action == "attack":
                    if "boss" in room and room["boss"].is_alive():
                        hero.attack(room["boss"])
            
                        if not room["boss"].is_alive():
                            print(f"THE {room['boss'].name.upper()} HAS FALLEN!")
                            hero.gain_xp(room["boss"].xp_reward)
                        else:
                            print(f"{room['boss'].name} counters your strike!")
                            damage = room["boss"].attack_power
                            hero.current_hp -= damage
                            print(f"You take {damage} damage! HP: {hero.current_hp}/{hero.max_hp}")
                            if hero.current_hp <= 0:
                                print("\nYOUR JOURNEY ENDS HERE...")
                                print("The darkness of the dungeon consumes your soul.")
                                game_running = False
                    else:
                        print("There is not`hi`ng here to attack but the cold, unyielding air.")

                elif action == "exit":
                    print("Farewell, traveler...")
                    return False

            
        case "load":
            print("\nLoading ancient scrolls (Saved File)...")
        case "exit":
            print("\nFarewell, traveler. The realm awaits your return.")
            pygame.mixer.music.fadeout(2000)
            pygame.time.wait(2000)
            pygame.quit()

if __name__ == "__main__":
    main()
