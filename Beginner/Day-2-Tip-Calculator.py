print('Welcome to the tip calculator')
totalBill = float(input('What was the total bill? $'))
tipPercentage = int(input('What percentage tip would you like to give? 10, 12, or 15? \n'))
noOfPeople = int(input('How many people to split the bill?\n'))

totalTip = totalBill * (tipPercentage/100)
billPerPerson = float((totalBill + totalTip)/noOfPeople)

print(f'Each person should pay: ${billPerPerson}')