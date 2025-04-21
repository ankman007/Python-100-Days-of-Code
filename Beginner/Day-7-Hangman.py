import random
from Beginner.Modules import py_art
from Modules import Data

print(py_art.hangman)
word_chosen = random.choice(Data.word_list)
word_length = len(word_chosen)
display = ['_'] * word_length

end_of_the_game = False
no_of_lives = 6

while not end_of_the_game:
    user_choice = input('\n\nGuess a letter: ')
    user_choice_letter = user_choice[0]

    if user_choice_letter in display:
        print(f'You have already chosen {user_choice_letter}, try another letter.')
        continue

    for i in range(word_length):
        if word_chosen[i] == user_choice_letter:
            display[i] = user_choice_letter

    for letter in display:
        print(letter, end=' ')

    if '_' not in display:
        end_of_the_game = True
        print('\n\nHurray!! You have guessed all the letters correctly. You win!!')
        break

    if user_choice_letter not in word_chosen:
        no_of_lives -= 1
        print(f'\nYour guessed "{user_choice_letter}", that letter is not in the word. You lose a life.')
        print(py_art.stages[no_of_lives])

        if no_of_lives <= 0:
            print(f'\n\nThe word was {word_chosen}.')
            print('You lose!!')
            break
