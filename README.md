# Arcane Tales (アルケイン・テイルズ)

**Arcane Tales** is a terminal-based RPG built with Python. It features a custom D&D-inspired dice engine, a modular world system, and immersive audio transitions. Note that the project is not finished and does not reflect its fina state, I will continue to work on the project, adding functions such as saving the game, more in depth classes for weapons, enemies, etc, this can be thought as a form of beta or tutorial.

## Features
* **Dynamic Character Creation:** 5 unique classes (Vanguard, Runeweaver, Apothecary, Silent Step, Spellblade) with randomly rolled stats.
* **D&D Mechanics:** D20 dice system for combat and room scanning, featuring Critical Successes and Failures.
* **World Engine:** A modular map system with 5 distinct rooms and a final boss encounter.
* **Immersive Audio:** Ambient background music using `pygame` with smooth fade-in/fade-out transitions.
* **OOP Architecture:** Clean, modular separation of concerns across `Player`, `Enemy`, and `Menu` modules.

### Visuals
<img width="686" height="809" alt="Screenshot 2026-03-22 142647" src="https://github.com/user-attachments/assets/3064cbff-b278-4ab4-b00c-d105d62715c3" />
<img width="657" height="805" alt="Screenshot 2026-03-22 142655" src="https://github.com/user-attachments/assets/4c849a84-4ba2-4733-abcb-696ccbce78d3" />
<img width="787" height="307" alt="Screenshot 2026-03-22 142707" src="https://github.com/user-attachments/assets/090bdf40-08e5-48f0-aea5-02292490d187" />
<img width="1670" height="516" alt="Screenshot 2026-03-22 142718" src="https://github.com/user-attachments/assets/64c0c431-1278-4ddc-b8e1-fc4068ba75f0" />
<img width="1013" height="605" alt="Screenshot 2026-03-22 142727" src="https://github.com/user-attachments/assets/90045c25-6042-4982-bb33-cec4d07f0666" />
<img width="1045" height="783" alt="Screenshot 2026-03-22 142735" src="https://github.com/user-attachments/assets/ff632f46-1ccf-4ead-8aa2-f9918074c19d" />
<img width="1181" height="293" alt="Screenshot 2026-03-22 142746" src="https://github.com/user-attachments/assets/5100f1e2-07d2-411b-ae77-0873f16fd5d2" />
<img width="1018" height="720" alt="Screenshot 2026-03-22 142839" src="https://github.com/user-attachments/assets/e08dd6bd-2f1a-48b5-bfd0-0892f30c64a0" />

## Installation & Setup

### Prerequisites
* [Python 3.12+](https://www.python.org/downloads/)
* [uv](https://github.com/astral-sh/uv) (Fast Python package manager)

### Setup Instructions

1. **Clone the repository:**
```powershell
git clone https://github.com/fermerazz/arcane_tales.git
cd arcane_tales
```

2. **Install dependencies:**
```powershell
uv add pygame
```

3. **Add audio:**
Place an MP3 file named `soundtrack.mp3` in the root folder. *(Note: A sample track is included).*

## How to Play

Run the game using the `uv` tool:
```powershell
uv run main.py
```

### In-Game Commands
* **Scan:** Search for secrets using Intelligence/Perception.
* **Move:** Navigate between rooms (North, South, East, West).
* **Stats:** View your character record and inventory.
* **Attack:** Engage in turn-based combat with enemies.
* **Exit:** Safely close the game and fade out the music.

## Technical Details
* **Architecture:** Object-Oriented Programming (OOP)
* **Engine:** Custom Python logic for state management and dice-rolling.
* **Environment:** Developed on Windows with `uv` package management.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Credits
Developed by Fermerazz with the guidance of Boots the Wizard Bear and the Boot.dev community.

