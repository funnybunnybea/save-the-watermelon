# Save the Watermelon Design

## Problem Description 
A terminal-based word guessing game. The intended player is a casual player wanting a quick word game like the NYT Wordle game. The player is trying to get the correct word by guessing letters that will reveal pieces of the word or remove slices from the watermelon if the letters are not in the word.
## Game Rules
Start: the program picks a random word and shows its letters as underscores.
Guess: the player guesses one letter at a time.
Correct guess: every matching letter is revealed and no slice is lost.
Incorrect guess: one slice is lost and the remaining slices are shown.
Invalid or repeated guess: an error message is shown, but no slice is lost.
Win: all letters are revealed.
Lose: slices reach 0.
## Program Data
secret_word: string chosen from the WORDS list
guessed_letters: set of letters already guessed
slices: integer, starts at 6
revealed word: built from secret_word and guessed_letters each turn

## Program Organization
pick_word(): returns a random word from the WORDS list
get_display(word, guessed): returns the word with unguessed letters as underscores
check_guess(guess, guessed): returns an error message, or empty text if valid
is_won(word, guessed): returns True if every letter is guessed
play_game(): starts one full game
main(): runs games until the player stops

## Program Flow
Start, Select Word, Display Hidden Word, Get Guess, Validate Guess, Update Game, Check Win/Loss, Repeat or End, Ask Play Again
