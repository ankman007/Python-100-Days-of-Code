import random

from Beginner.Modules import py_art

print(py_art.number_guessing_game)

print('Welcome to Number Guessing Game!')
number_to_guess = random.randint(1, 101)
difficulty_choice = input("Choose the difficulty for the game. Type 'easy' or 'hard': ")
attempts = 5
if difficulty_choice == 'easy':
    attempts = 10


def decrease_attempts(lives):
    return lives - 1


def user_guess_wrong(high_or_low, lives_left):
    print(f'{high_or_low} Guess again')
    decrease_attempts(lives_left)


print("I'm thinking of a number between 1 and 100.")

while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    user_guess = int(input('\nMake a guess: '))

    if user_guess == number_to_guess:
        print(f'\nYou got it! The answer was {number_to_guess}.')
        break

    elif user_guess != number_to_guess:
        if user_guess > number_to_guess:
            user_guess_wrong('Too High.', attempts)
        elif user_guess < number_to_guess:
            user_guess_wrong('Too Low.', attempts)





