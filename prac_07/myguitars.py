"""
CP1404 - Guitar file reader and display
Name: Casey Summers
Expected time: 45m
Actual time:
"""

from guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    """Program to store list of objects from .csv file and display them in descending year order."""
    guitars = load_guitars_from_csv(FILENAME)
    guitars.sort()
    print("Guitars List.")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_string}")


def load_guitars_from_csv(filename):
    """Loads the .csv and sorts objects into list using Guitar class."""
    guitars = []
    with open(filename, 'r') as in_file:
        csv_reader = csv.reader(in_file)
        for row in csv_reader:
            try:
                name, year, cost = row
                year = int(year)
                cost = float(cost)
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
            except IndexError:
                print("Invalid index.")
        return guitars


if __name__ == '__main__':
    main()
