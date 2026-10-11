import random
from words import WORDS


def pick_word():
    """Return a random secret word from word list."""
    return random.choice(WORDS)


def get_display(word, guessed):
    """Return the word with unguessed letters shown as underscores."""
    shown = []
    for letter in word:
        if letter in guessed:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


def check_guess(guess, guessed):
    """Return an error message if the guess is invalid, otherwise empty text."""
    if len(guess) != 1:
        return "Enter exactly one letter."
    if not guess.isalpha():
        return "Letters only, no numbers or symbols."
    if guess in guessed:
        return "You already guessed that letter."
    return ""


def is_won(word, guessed):
    """Return True if every letter in the word has been guessed."""
    for letter in word:
        if letter not in guessed:
            return False
    return True
