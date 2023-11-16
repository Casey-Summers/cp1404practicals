"""
CP1404 - Taxi class and client test
Name: Casey Summers
Expected: 15m
Actual: 10m
"""

from prac_09.taxi import Taxi


def main():
    """Program to test specialised Taxi child class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


if __name__ == '__main__':
    main()
