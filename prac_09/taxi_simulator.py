"""
CP1404 - Taxi simulator program using Taxi and SilverServiceTaxi classes
Expected: 140m
Actual:
"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose, d)rive\n"


def main():
    """Program to add Taxi two different types of Taxi objects and calculate fares using accordingly."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fare = 0

    print("Let's drive!")
    choice = input(f"{MENU}>>> ").lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice > len(taxis) - 1:
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[taxi_choice]
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                try:
                    if current_taxi.fanciness:
                        fare = current_taxi.calculate_fare()  # fare for SilverServiceTaxi class
                    else:
                        fare = current_taxi.get_fare()  # fare for Taxi class
                except AttributeError:
                    print("Attribute Error.")
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                total_fare += fare
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_fare:.2f}")
        choice = input(f"{MENU}>>> ").lower()
    print(f"Total trip cost: ${total_fare:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the text for taxi selection."""
    for taxi_number, taxi in enumerate(taxis):
        print(f"{taxi_number} - {taxi}")


if __name__ == '__main__':
    main()
