print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? $'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? \n'))
no_of_people = int(input('How many people to split the bill?\n'))

total_tip = total_bill * (tip_percentage/100)
bill_per_person = float((total_bill + total_tip)/no_of_people)

print(f'Each person should pay: ${bill_per_person}')