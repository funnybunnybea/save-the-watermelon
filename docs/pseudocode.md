start main
  repeat
      call play_game
      ask if they wanna play again
    until player answer no(case insensitive)
    if answer yes
      start game
    elif answer no
      end main
    else
      display input error

dis play_game
  secret_word = random word from WORDS
  guessed_letters = empty set
  slices = 6
  while slices > 0 and word not revealed
    show unguessed letters as udnerscore
    show slice left
    ask fro guess, convert lowercase
    error = Call check_guess
      show error
      go back to top, no slices lost
    add guess to guessed letters 
    if guess in secret_word
      change correct underscores into guess
      print "correct"
    else 
      slices = slices-1
      print "wrong" 
if word fully revealed 
  print "win"
else
  print "lose"
  reveal secret word
End play_game

dis check_guess(guess, guessed_letters)
    if guess length is not 1 then return "enter one letter"
    if guess is not a letter then return "letters only"
    if guess is in guessed_letters then return "already guessed"
    return empty text
end check_guess

dis is_won(word, guessed_letters)
    FOR each letter in word
        if letter is not in guessed_letters then return False
    return True
end is_won
