"""
CLI Hangman game
"""

import random
import hangman_assets as Assets

word_list = Assets.WORD_LIST
stages = Assets.STAGES

chosen_word: str = random.choice(word_list)
tries_left = len(stages)
display: list[str] = list("_" * len(chosen_word))
print(Assets.CLEAR)
print(Assets.LOGO)

while "_" in display and tries_left > 1:
    print()
    print(*display, sep = " ")
    print(stages[tries_left - 1])

    guess: str = str(input("Guess a letter: "))[0].lower()
    success: bool = False
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            success = True
            display[index] = letter

    if not success:
        print(f"You guessed {guess}, that is not in the word. You loose a life.")
        tries_left -= 1

if "_" not in display:
    print(Assets.WIN)
else:
    print(Assets.LOSE)
    print(f"The word was: {chosen_word}")
print(*display, sep = " ")
print(stages[tries_left - 1])
