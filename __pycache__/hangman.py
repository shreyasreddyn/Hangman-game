import random
current_streak = 0
best_streak = 0
from words import word_list
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "".join([" " if char == " " else "_" for char in word])
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print(Style.BRIGHT + Fore.CYAN + "Let's play Hangman!")
    print(display_hangman(tries))
    print(" ".join(word_completion))
    print("\n")

    while not guessed and tries > 0:
        guess = input(Fore.YELLOW + "Please guess a letter or word: ").strip().upper()

        if not guess:
            print(Fore.YELLOW + "Input cannot be empty.")
            continue
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(Fore.YELLOW + f"You already guessed the letter {guess}")
            elif guess not in word:
                print(Fore.RED + f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(Fore.GREEN + f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(Fore.YELLOW + f"You already guessed the word {guess}")
            elif guess != word:
                print(Fore.RED + f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print(Fore.YELLOW + "Not a valid guess.")

        print(display_hangman(tries))
        print(" ".join(word_completion))
        print("\n")

    if guessed:
        print(Fore.GREEN + "🎉 Congrats, you guessed the word! You win!")
    else:
        print(Fore.RED + f"💀 Sorry, you ran out of tries. The word was '{word}'. Maybe next time!")

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]


def save_best_streak(streak):
    with open("streak.txt", "w") as file:
        file.write(str(streak))

    word = get_word()
    play(word)
    while input(Fore.CYAN + "Play Again? (Y/N) ").strip().upper() == "Y":
        word = get_word()
        play(word)
def main():
    global current_streak, best_streak

    while True:
        word = get_word()
        won = play(word)

        if won:
            current_streak += 1
            best_streak = max(best_streak, current_streak)
            print(Fore.MAGENTA + f"🔥 Current Streak: {current_streak}")
            print(Fore.MAGENTA + f"🏆 Best Streak: {best_streak}")
        else:
            current_streak = 0
            print(Fore.MAGENTA + "💔 Streak reset to 0.")

        again = input(Fore.CYAN + "Play Again? (Y/N) ").strip().upper()
        if again != "Y":
            print(Fore.CYAN + "Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()   