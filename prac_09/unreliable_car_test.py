"""
CP1404 - UnreliableCar class and client test
Name: Casey Summers
Expected: 20m
Actual: 30m
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Program to test specialised UnreliableCar child class."""
    reliable_car = UnreliableCar("Holden", 100, 80.1)
    unreliable_car = UnreliableCar("Ford", 40, 20.2)
    reliable_car.drive(50)
    unreliable_car.drive(50)
    print(reliable_car)
    print(unreliable_car)


if __name__ == '__main__':
    main()
