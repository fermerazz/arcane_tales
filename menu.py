import pygame

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
           Welcome to ARCANE TALES!
             (アルケイン・テイルズ)
                   Main Menu
          """)
    print("1. Start Game")
    print("2. Load Game")
    print("3. Exit to Desktop")
    print("4. Toggle Music")
    

    while True:
        choice = input("Greetings traveler! What is your choice? > ")

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