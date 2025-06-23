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

## ▶️ How to Run the Game

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/hangman-game.git
    cd hangman-game
    ```

2. **Install dependencies**:

    ```bash
    pip install colorama
    ```

3. **Make sure you have a `words.py` file** like this in the same folder:

    ```python
    word_list = ["apple", "banana", "grape", "python", "hangman"]
    ```

4. **Run the game**:

    ```bash
    python hangman.py
    ```
    
## Project Structure
hangman-game/
├── hangman.py    
├── words.py       
├── streak.txt     
└── README.md       

## To-Do / Future Improvements
1.Add GUI using tkinter
2.Add difficulty levels (Easy, Medium, Hard)
3.Export score history to a file
4.Show time taken per game
5.Leaderboard with high scores

