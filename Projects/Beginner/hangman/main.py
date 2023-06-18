from random import choice
from word_list import wordlist

playing = True
WORD = choice(wordlist)
wrong_guesses = []
guesses = []

while playing:
    word_str = ''
    for char in WORD:
        if char.upper() in guesses:
            word_str += char.upper() + " "
        else:
            word_str += '_ '
    print(f"Word: {word_str}")
    if "_" not in word_str:
        print("You WON!")
        print(f"You had {len(wrong_guesses)} wrong guesses")
        break
    if len(wrong_guesses) > 7:
        print("You LOST!")
        print("You made 8 mistakes.")
        print(f"Your word was: {WORD}")
        break
    guess_str = ', '.join(str(e) for e in wrong_guesses)
    print(f"Your wrong guesses: {guess_str}")
    guess = input("Your guess: ")
    while not (guess.isalpha() and len(guess) == 1):
        print("Your guess must be a letter!")
        guess = input("Your guess: ")
    if guess.upper() in guesses:
        print(f"You already guessed the letter {guess.upper()}")
    elif guess not in WORD:
        wrong_guesses.append(guess.upper())
    print("\n")
    if guess in WORD and guess.upper() not in guesses:
        print("Your guess was correct!")
    elif guess not in WORD and guess.upper() not in wrong_guesses:
        print("Your guess was wrong!")
    guesses.append(guess.upper())


        