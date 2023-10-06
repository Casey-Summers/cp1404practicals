"""
CP1404 - List exercise
Name: Casey Summers
"""

numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    """Program to get valid user and gather 5 numbers then printing information about them."""
    username = input("Username: ")  # Was told to have both program in same file, figured this was a good way.
    while username not in usernames:
        print("Access denied")
        username = input("Username: ")
    print("Access granted")
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    display_number_info()


def display_number_info():
    """Display information about numbers inside list."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average}")


main()
