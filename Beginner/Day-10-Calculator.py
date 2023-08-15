from Modules import PyArt

print(PyArt.calculator_logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    if n1 > n2:
        return n1 - n2
    return n2 - n1


def divide(n1, n2):
    if n1 > n2:
        return n1 / n2
    return n2 / n1


def multiply(n1, n2):
    return n1 * n2


operation = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply
}

continue_choice = 'yes'

while continue_choice == 'yes':
    num1 = int(input("\nEnter the first number: "))
    num2 = int(input("Enter the second number: "))
    print('')

    for symbol in operation:
        print(symbol, end="     ")
    operation_symbol = input("\nPick an operation from the line above: ")

    calc = operation[operation_symbol]
    result = calc(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")
    continue_choice = input('\nDo you want to perform another operation? [yes / no]\n')
