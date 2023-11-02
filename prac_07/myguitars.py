"""
CP1404 - Guitar file reader and display
Name: Casey Summers
Expected time: 45m
Actual time: 65m
"""

from guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    """Program to store list of objects from .csv file and display them in descending year order."""
    guitars = load_guitars_from_csv(FILENAME)
    guitars.sort()
    print("Guitars List.")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input(f"\nName: ")

    # Display Guitar list
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_string}")

    save_guitars_to_file(guitars)
    print(f"\nGuitars saved to {FILENAME}")


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


def save_guitars_to_file(guitars):
    """Save lists of class objects back into the file with the same format."""
    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == '__main__':
    main()
