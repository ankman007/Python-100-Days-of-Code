from Beginner.Modules import py_art
from Modules import Data

print(py_art.caesar_cypher)
print(Data.alphabet)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def caesar(user_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in user_text:
        position = Data.alphabet.index(letter)
        new_position = position + shift_amount
        end_text += Data.alphabet[new_position]

    print(f'\nThe {cipher_direction}d text is {end_text}.')


caesar(text, shift, direction)

