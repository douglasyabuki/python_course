"""
Create a game where the user has to guess
the secret word.
- You will define a secret word and allow the user
  to input only one letter at a time.
- When the user enters a letter, check if it is
  in the secret word.
    - If the letter is in the secret word, display the letter.
    - If the letter is not in the secret word, display *.
Count the number of attempts made by the user.
"""
import os

secret_word = 'perfume'
guessed_letters = ''
attempt_count = 0

while True:
    entered_letter = input('Enter a letter: ')
    attempt_count += 1

    if len(entered_letter) > 1:
        print('Enter only one letter.')
        continue

    if entered_letter in secret_word:
        guessed_letters += entered_letter

    formed_word = ''
    for secret_letter in secret_word:
        if secret_letter in guessed_letters:
            formed_word += secret_letter
        else:
            formed_word += '*'

    print('Word formed:', formed_word)

    if formed_word == secret_word:
        os.system('clear')  # Use 'cls' instead of 'clear' if on Windows
        print('YOU WON!! CONGRATULATIONS!')
        print('The secret word was:', secret_word)
        print('Attempts:', attempt_count)
        guessed_letters = ''
        attempt_count = 0
