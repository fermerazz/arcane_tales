# Arcane Tales (アルケイン・テイルズ)

**Arcane Tales** is a terminal-based RPG built with Python. It features a custom D&D-inspired dice engine, a modular world system, and immersive audio transitions.

## Features
- **Dynamic Character Creation**: 5 unique classes (Vanguard, Runeweaver, Apothecary, Silent Step, Spellblade) with randomly rolled stats.
- **D&D Mechanics**: D20 dice system for combat and room scanning, featuring Critical Successes and Failures.
- **World Engine**: A modular map system with 5 distinct rooms and a final boss encounter.
- **Immersive Audio**: Ambient background music using `pygame` with smooth fade-in/fade-out transitions.
- **OOP Architecture**: Clean, modular separation of concerns across `Player`, `Enemy`, and `Menu` modules.

## Installation & Setup

### Prerequisites
- [Python 3.12+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (Fast Python package manager)

### Setup
1. **Clone the repository**:
```powershell
git clone https://github.com/fermerazz/arcane_tales.git
cd arcane_tales

Install Dependencies:
uv add pygame

Add Audio:
Place an MP3 file named theme.mp3 in the root folder.
🎮 How to Play
Run the game using the uv tool:

uv run main.py

Commands
Scan: Search for secrets using Intelligence/Perception.
Move: Navigate between rooms (North, South, East, West).
Stats: View your character record and inventory.
Attack: Engage in turn-based combat with enemies.
Exit: Safely close the game and fade out the music.

Technical Details
Architecture: Object-Oriented Programming (OOP)
Engine: Custom Python logic for state management and dice-rolling.
Environment: Developed on Windows with uv package management.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Credits
Developed by Fermerazz with the guidance of Boots the Wizard Bear and the Boot.dev community.

