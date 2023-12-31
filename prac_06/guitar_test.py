"""
CP1404 Practical - Client code to use the guitar class.
Name: Casey Summers
Estimated time: 25m
Actual time: 27m
"""

from prac_06.guitar import Guitar


def main():
    """Program to test guitar class with expected outcome checker."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 800.00)
    print(f"{gibson}\n")  # Test f-string formatting

    # Test get_age() method
    print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age()}")

    # Test is_vintage() method
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


main()
