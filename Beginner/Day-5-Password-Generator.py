from Modules import Data
import random

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(Data.alphabets)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(Data.symbols)

for char in range(1, nr_numbers):
    password_list += random.choice(Data.numbers)

random.shuffle(password_list)
password = ''.join(password_list)
print(f"\nYou password is: {password}")

