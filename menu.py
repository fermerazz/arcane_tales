import pygame
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def toggle_music(is_paused):
    if is_paused:
        pygame.mixer.music.unpause()
        print("--- Music resumed! ---")
        return False 
    else:
        pygame.mixer.music.pause()
        print("--- Music muted. ---")
        return True 

def show_main_menu(is_paused):
    #This function will print the main menu screen and captures user input
    print(r"""
                           o
                       _---|         _ _ _ _ _
                    o   ---|     o   ]-I-I-I-[
   _ _ _ _ _ _  _---|      | _---|    \ ` ' /
   ]-I-I-I-I-[   ---|      |  ---|    |.   |
    \ `   '_/       |     / \    |    | /^\|
     [*]  __|       ^    / ^ \   ^    | |*||
     |__   ,|      / \  /    `\ / \   | ===|
  ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
  I_I__I_I__I_I  (====(_________)___|_|____|____
  \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_|
   |[]      '|   | []  |`__  . [  \-\--|-|--/-/
   |.   | |' |___|_____I___|___I___|---------|
  / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] |
 <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \
 ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===>
 ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [
 <===>     ' ||||| |   |   | ||||.||  []   <===>
  \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/
   |      . _||||| |   |   | ||||.|| |     | |
../|' v . | .|||||/____|____\|||| /|. . | . ./
.|//\............/...........\........../../\\\
        Welcome to ARCANE TALES, have fun!
              (アルケイン・テイルズ)
                   Main Menu
          """)
    print("1. Start Game")
    print("2. Load Game")
    print("3. Exit Game")
    print("4. Toggle Music")
    

    while True:
        choice = input("\nGreetings traveler! What is your choice? > ")

        if choice == "1":
            return "start", is_paused
        elif choice == "2":
            return "load", is_paused
        elif choice == "3":
            return "exit", is_paused
        elif choice == "4":
            is_paused = toggle_music(is_paused)
        else:
            print("Oh no! The ancient runes reject that option!. Try 1, 2, 3 or 4.")

def show_pause_menu(is_paused):
    #This function displays the pause menu and captures user input
    print(r""" 
                   (   .                   _ _ _ _ _
    (   .     .  .=##                      ]-I-I-I-[                    
  .=##   .  (      ( .                     \ `  ' /        
    ( .   .=##  .       .                   |'  []          
  .     .   ( .    .        _----|          |.  '|           
                             ----|_----|    | ' .|           
    _ _ _ _ _ _      _----|      | ----|    | [] |         
    ]-I-I-I-I-[       ----|      |     |    |. ` |          
     \ `   '_/            |     / \    |    | /^\|            
      []  `__|            ^    / ^ \   ^    | |*||                 
      |__   ,|           / \  / ^ ^`\ / \   | ===|                 
   ___| ___ ,|__        / ^  /=_=_=_=\ ^ \  |, `_|
   I_I__I_I__I_I       (====(_________)_^___|____|____
   \-\--|-|--/-/       |     I  [ ]__I I_I__|____I_I_|
    |[] `    '|__   _  |_   _|`__  ._[  _-\--|-|--/-/
   / \  [] ` .|  |-| |-| |-| |_| |_| |_| | []   [] |
  <===>    `  |.            .      .     |    '    |
  ] []|  `    |   []    --   []      `   |   [] '  |
  <===>.  `   |  .   '  .       '  .[]   | '       |
   \_/    .   |       .       '          |   `  [] |
    | []    . |   .  .           ,  .    | ,    .  |
    |    . '  |       . []  '            |    []'  |
   / \   ..   |  `      .    .     `[]   | -   `   |
  <===>      .|=-=-=-=-=-=-=-=-=-=-=-=-=-|    .   / \
  ] []|` ` [] |`  .  .   _________   .   |-      <===>
  <===>  `  ' | '   |||  |       |  |||  |  []   <===>
   \_/     -- |   . |||  |       |  |||  | .  '   \_/
  ./|' . . . .|. . .||||/|_______|\|||| /|. . . . .|\_    
          
            Hi Traveler, what do you wish to do?  
        """)
    print("1. Resume Game")
    print("2. Save Game")
    print("3. Exit to Main Menu")
    print("4. Toggle Music")

    while True:
        choice = input("What is your choice, wanderer? > ")

        if choice == "1":
            return "resume", is_paused
        elif choice == "2":
            return "save", is_paused
        elif choice == "3":
            return "main_menu", is_paused
        elif choice == "4":
            is_paused = toggle_music(is_paused)
        else:
            print("Uh oh! The book of knowledge declined that option!. Try 1, 2, 3 or 4.")

def show_character_creation():
    print(r"""
                 __
               .'/\'.
             .'-/__\-'.
           .'--/____\--'.
         .'--./______\.--'.
       .'--../________\..--'.
     .'--.._/__________\_..--'.
   .'--..__/____________\__..--'.
 .'--..___/______________\___..--'.
'========'================'========'
      [_|__]            [_|__]             
     =[__|_]=====""=====[__|_]==.
      [_|__]     '|     [_|__]  |
      [__|_]     |'     [__|_]  |
      [_|__]  .--JL--.  [_|__]  '===O
      [__|_]   \====/   [__|_]
      [_|__]_.-| .; |-._[_|__]
      [__|_]'._ \__/(_.'[__|_]
      [.-._]            [_.-.]
      [_.-.'--..____..--'.-._]
 (o)  [(_.'   .-.     .-.'._)\ (o)
(\'/) [  .-. (_.'.-. (_.' .-.](\'/)
   ;: [ (_.'.-. (_.' .-. (_.'| ;:'
;:    [ .-. '._) .-. '._).-. ]   ;:.
      [(_.'  .-. '._) .-.'._)]
  (o) /.-.  (_.'.-.  (_.' .-.];:(o)
 (\'/)['._).-. (_.'   .-.(_.'] (\'/)
      [   (_.'.-.  .-.'._)   \ ;:
;:'   '-._    '._) '._)   _.-'
  LGB      `---..____..---'   ;:`
   ;:'      ;:'.:;     ;;"
          
You are about to enter the magical lands, but before...
          """)
    while True:
        name = input("What is your name, hero? > ").strip()
        if name.isalpha():
            break
        else:
            print("\nThe ancient scrolls only accept names written in the common tongue (letters only)!\n")
        
    while True:
        clear_screen()

        print(f"\nWell, nice to meet you {name}! Now it's time to choose your path > ")
        print("1. The Vanguard (Strength & Steel)")
        print("2. The Runeweaver (Arcane Knowledge)")
        print("3. The Apothecary (Nature & Alchemy)")
        print("4. The Silent Step (Agility & Shadows)")
        print("5. The Spellblade (Steel & Sorcery)")
        
        inspect_choice = input("What class do you wish to learn about, hero? > ").strip()
        player_class = ""

        match inspect_choice:
            case "1":
                print("\n--- THE VANGUARD ---")
                print("Vibe: A seasoned frontline fighter who relies on heavy armor and martial mastery.")
                print("Stats Focus: High strength and Constitution.")
                print("Playstyle: Brutal, straightforward combat. They excel at shattering enemy armor, wielding massive weapons, and enduring heavy hits that would crush a weaker traveler.")
                player_class = "vanguard"
            
            case "2":
                print("\n--- THE RUNEWEAVER ---")
                print("Vibe: A scholar of ancient, forgotten magic.")
                print("Stats Focus: High Intelligence and Mana.")
                print("Playstyle: Exploiting elemental weaknesses. They require the player to recall and decipher ancient runic scripts to cast devastating magical bursts from a distance.")
                player_class = "runeweaver"

            case "3":
                print("\n--- THE APOTHECARY ---")
                print("Vibe: A master of the physical and chemical world, blending science with nature.")
                print("Stats Focus: High Intelligence and Dexterity.")
                print("Playstyle: Tactical and prepared. They excel at creating lasting effects, like burning aromatic woods to ward off dark spirits, or brewing potent elixirs that heal wounds over time.")
                player_class = "apothecary"

            case "4":
                print("\n--- THE SILENT STEP ---")
                print("Vibe: A scout and assassin who strikes before the enemy even knows they are there.")
                print("Stats Focus: High Dexterity and Perception.")
                print("Playstyle: High risk, high reward. They excel at evasion and striking from the shadows for massive critical damage, but they cannot take many hits in a fair fight.")
                player_class = "silent_step"
            
            case "5":
                print("\n--- THE SPELLBLADE ---")
                print("Vibe: A hybrid warrior who channels raw magical energy through their weapons.")
                print("Stats Focus: Balanced Strength and Intelligence.")
                print("Playstyle: Ultimate versatility. They can fluidly switch between physical sword strikes and close-range magical attacks depending on what the enemy is most vulnerable to.")
                player_class = "spellblade"
            
            case _:
                print("The stars do not align with that choice, hero. Try 1-5.")
                input("\nPress Enter to try again...")
                continue

        while True:
            print(f"\nDo you wish to walk the path of the {player_class}?")
            confirm = input("Type 'y' to confirm, or 'n' to inspect another class > ").strip().lower()

            if confirm == 'y':
                break
            elif confirm == 'n':
                print("\nLet us look at the other paths...")
                break
            else:
                print("\nAha! The wise kitten with a hat caught you wandering around! Please choose between 'y' or 'n'")
        
        if confirm == 'y':
            break

    print(f"\nAh... {name} the {player_class.capitalize()}. The prophecies spoke of your arrival.")
    return name, player_class