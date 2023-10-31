"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = "C - Convert Celsius to Fahrenheit \n" \
       "F - Convert Fahrenheit to Celsius \n" \
       "Q - Quit"


def main():
    """Program with menu to convert between Celsius and Fahrenheit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.1f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert between Fahrenheit and Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    """Convert between Celsius and Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
