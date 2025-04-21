from Beginner.Modules import py_art
from Modules import Data
import random


def increase_points(points):
    return points + 1


def determine_higher_follower(account1, account2, score_count):
    if account1['follower_count'] > account2['follower_count']:
        print(f"You were correct.")
        return increase_points(score_count)
    else:
        return False


score = 0
correct_answer = True
print(py_art.higher_lower_logo)

while correct_answer:
    ig_account1 = random.choice(Data.ig_details)
    ig_account2 = random.choice(Data.ig_details)

    print(f"Compare A: {ig_account1['name']}, {ig_account1['description']}, from {ig_account1['country']}.", end='')
    print(py_art.vs)
    print(f"Compare B: {ig_account2['name']}, {ig_account2['description']}, from {ig_account2['country']}.")

    user_choice = input('\nWho has more followers? [ A / B ]\n')
    if user_choice == 'A':
        score = determine_higher_follower(ig_account1, ig_account2, score)
    elif user_choice == 'B':
        correct_answer = determine_higher_follower(ig_account2, ig_account1, score)

print(f"\nSorry, that's wrong. Final score: {score}")
