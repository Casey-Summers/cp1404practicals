"""
CP1404 - Taxi simulator program using Taxi and SilverServiceTaxi classes
Expected: 140m
Actual:
"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose, d)rive\n"


def main():
    """___"""
    print("Let's drive!")
    choice = input(f"{MENU}>>> ").lower()
    while choice != 'q':
        taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
        if choice == 'c':
            print("c")
        elif choice == 'd':
            print("D")
        else:
            print("Invalid Input")
        choice = input(f"{MENU}>>> ").lower()
    print("Exiting. Thank you")


if __name__ == '__main__':
    main()
