from logic import pick_word, get_display, check_guess, is_won
from words import STARTING_SLICES


def play_game():
    """Run one full game of Save the Watermelon."""
    word = pick_word()
    guessed = set()
    slices = STARTING_SLICES

    while slices > 0 and not is_won(word, guessed):
        print("\n" + get_display(word, guessed))
        print("Slices left:", slices)
        guess = input("Guess a letter: ").strip().lower()

        error = check_guess(guess, guessed)
        if error != "":
            print(error)  # invalid input costs no slice
            continue

        guessed.add(guess)
        if guess in word:
            print("Correct!")
        else:
            slices -= 1
            print("Wrong! You lost a slice.")

    if is_won(word, guessed):
        print("\nYou saved the watermelon! The word was", word)
    else:
        print("\nNo slices left. The word was", word)


def main():
    """Play games until the player chooses to stop."""
    play_again = "yes"
    while play_again == "yes":
        play_game()
        play_again = input("Play again? (yes/no): ").strip().lower()
    print("Thanks for playing!")


main()
