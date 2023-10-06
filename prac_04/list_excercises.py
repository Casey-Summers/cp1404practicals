"""
CP1404 - List exercise
Name: Casey Summers
"""

numbers = []


def main():
    """Program to gather 5 numbers and print information about them."""
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
