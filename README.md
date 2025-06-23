# Hangman-game
Used flask and the game can be played in cmd
# 🎮 Hangman Game (Python)

A terminal-based version of the classic Hangman game written in Python! Guess the word one letter at a time before the stickman meets his fate.

---

## 🧠 Features

- Randomly selected words from a custom list
- Tracks your **current win streak** and **best streak** (saved to file)
- Colorful terminal output using `colorama`
- ASCII art to display hangman stages
- Input validation and replay option

---

## 🖥️ Requirements

- Python 3.6 or higher
- `colorama` library

To install `colorama`, run:
pip install colorama

How to Run the Game
1.Clone the repository:
git clone https://github.com/your-username/hangman-game.git
cd hangman-game
Make sure you have a words.py file.
Run the game:
python hangman.py

Project Structure
hangman-game/
├── hangman.py
├── words.py
├── streak.txt
└── README.md

To-Do / Future Improvements
 Add GUI using tkinter
 Add difficulty levels (Easy, Medium, Hard)
 Export score history to a file
 Show time taken per game
 Leaderboard with high scores

