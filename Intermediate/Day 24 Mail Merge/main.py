with open(file='Input/Names/invited_names.txt', mode='r') as names:
    names = names.readlines()
    no_of_names = len(names) - 1

with open(file='Input/Letters/starting_letter.txt', mode='r+') as txt:
    txt = txt.read()

    for name in names:
        stripped_name = name.strip()
        new_txt = txt.replace('[name]', f'{stripped_name}')

        with open(file=f'Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_txt)

