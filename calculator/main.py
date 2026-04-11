from art import calc_logo


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


def square(n1, n2):
    return n1**n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': square
}


def calculator():
    calculate_start = True
    print(calc_logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    while calculate_start:
        operatation_symbol = input("Pick an operation from the line above?: ")
        function = operations[operatation_symbol]
        num2 = float(input("What's the next number?: "))
        first_result = function(num1, num2)
        print(f"{num1} {operatation_symbol} {num2} = {first_result}")
        next_message = input(
            f"Type 'y' to continue calculation with {first_result}, or type 'n' to exit.: ").lower()
        if (next_message == 'y'):
            num1 = first_result
            # operatation_symbol = input("Pick another operations?: ")
            # function = operations[operatation_symbol]
            # # num3 = int(input("What's the next number?: "))
            # second_result = function(num1, num2)
            # print(f"{num1} {operatation_symbol} {num2} = {second_result}")
        else:
            calculate_start = False
            calculator()


calculator()
# function = operations['+']
# result = function(2, 3)
# print(result)
