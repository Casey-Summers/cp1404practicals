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
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fare = 0

    print("Let's drive!")
    choice = input(f"{MENU}>>> ").lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            for taxi_number, taxi in enumerate(taxis):
                print(f"{taxi_number} - {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            get_valid_taxi_choice(taxi_choice, taxi_number)
            current_taxi = taxis[taxi_choice]
            print(current_taxi)
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi} trip cost you ${fare:.2f}")
                total_fare += fare
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_fare}")
        choice = input(f"{MENU}>>> ").lower()
    print("Exiting. Thank you")


def get_valid_taxi_choice(taxi_choice, taxi_number):
    while taxi_choice > taxi_number:
        return print("Invalid taxi choice")


# def get_valid_input(prompt):
#     user_input = input(prompt)
#     while user_input !=

if __name__ == '__main__':
    main()
