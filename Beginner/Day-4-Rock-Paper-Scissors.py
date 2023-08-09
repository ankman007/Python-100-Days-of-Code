import random
from Modules import PyArt

rock = PyArt.rock
paper = PyArt.paper
scissors = PyArt.scissors

user_choice_num = int(input('''
What do you want to choose?
1 => Rock
2 => Paper
3 => Scissors
'''))
computer_choice_num = random.randint(1, 3)

computer_choice = ''
user_choice = ''

if user_choice_num == 1:
    user_choice += rock
elif user_choice_num == 2:
    user_choice += paper
elif user_choice_num == 3:
    user_choice += scissors

print('\nYou chose:')
print(user_choice)

if computer_choice_num == 1:
    computer_choice += rock
elif computer_choice_num == 2:
    computer_choice += paper
else:
    computer_choice += scissors

print('Computer chose:')
print(computer_choice)

# 1-rock, 2-paper, 3-scissor
if user_choice_num == computer_choice_num:
    print('Draw.')

# for user_choice == rock
elif user_choice_num == 1:
    if computer_choice_num == 2:
        print('You lose.')
    elif computer_choice_num == 3:
        print('You win.')

# for user_choice == paper
elif user_choice_num == 2:
    if computer_choice_num == 1:
        print('You win.')
    elif computer_choice_num == 3:
        print('You lose.')

# for user_choice == scissors
elif user_choice_num == 3:
    if computer_choice_num == 1:
        print('You lose.')
    elif computer_choice_num == 2:
        print('You win.')
