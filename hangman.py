import tkinter as tk
import random


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word_list = ["python", "hangman", "programming", "computer", "keyboard", "developer"]
        self.secret_word = random.choice(self.word_list).lower()
        self.guesses = set()
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

        self.word_label = tk.Label(self.root, text=self.display_word(), font=("Helvetica", 16))
        self.word_label.pack(pady=10)

        self.guess_label = tk.Label(self.root, text="Guess a letter:", font=("Helvetica", 12))
        self.guess_label.pack()

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.entry_var, font=("Helvetica", 12), width=5)
        self.entry.pack()

        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.message_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.message_label.pack()

    def display_word(self):
        return " ".join(letter if letter in self.guesses else "_" for letter in self.secret_word)

    def make_guess(self):
        guess = self.entry_var.get().lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in self.guesses:
                self.message_label.config(text="You already guessed that letter.")
            elif guess in self.secret_word:
                self.guesses.add(guess)
                self.word_label.config(text=self.display_word())
                if set(self.secret_word) == self.guesses:
                    self.message_label.config(text="Congratulations! You guessed the word.")
                    self.disable_input()
            else:
                self.attempts_left -= 1
                self.message_label.config(text=f"Wrong guess! Attempts left: {self.attempts_left}")
                self.draw_hangman()

                if self.attempts_left == 0:
                    self.message_label.config(text=f"Sorry! You ran out of attempts. The word was {self.secret_word}.")
                    self.disable_input()
        else:
            self.message_label.config(text="Invalid input. Please enter a single letter.")

    def draw_hangman(self):
        print(f"Draw hangman here (attempts left: {self.attempts_left})")

    def disable_input(self):
        self.guess_button.config(state=tk.DISABLED)
        self.entry.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200") 
    hangman_game = HangmanGame(root)
    root.mainloop()
