# The Hangman game
# word = 'o n o m a t o p e e '
"""
if the starting and ending letter are found inside the word, then they must be visible
word = 'o _ o _ _ _ o _ e e'
7 tries
"""
from hangman_words import guess_words as word_list
import random


def parse_word(word_answer: str, replace_letter: str, hidden_word: list) -> list:
    for index, letter in enumerate(word_answer):
        if replace_letter == '_' and word_answer[0] != letter and word_answer[-1] != letter:
            hidden_word[index] = replace_letter
        elif letter == replace_letter:
            hidden_word[index] = replace_letter
    return hidden_word


def check_input(check_guess) -> str:
    if check_guess.isalpha() is False:
        return "Please enter a letter."
    elif len(check_guess) > 1:
        return "Your guess has too many characters. Please enter a letter."


answer = random.choice(word_list).lower()
word = list(answer)

word = parse_word(answer, "_", word)

step = ' '.join(word)
print(f"Guess the word: {step}")

used_letters = set()
tries = 0

while tries < 7:
    if len(used_letters) > 0:
        print(f"Already used letters: {','.join(used_letters)}")
    user_guess = input("Input a letter: ").lower()
    while user_guess.isalpha() is False or len(user_guess) > 1:
        print(check_input(user_guess))
        user_guess = input("Input a letter: ").lower()

    if user_guess not in answer:
        tries += 1
        used_letters.add(user_guess)
    elif answer[0] != user_guess and answer[-1] != user_guess:
        word = parse_word(answer, user_guess, word)
    if tries == 7:
        print(f"You lost. The answer was: '{answer}'")
    elif '_' not in word:
        print(f"You won! You guessed the word: '{answer}'.")
        break
    else:
        print(f"You have {7 - tries} tries left.")
        print(" ".join(word))
