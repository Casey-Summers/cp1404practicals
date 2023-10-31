"""
CP1404 Practical - Program to store a list of guitars and use the guitar class.
Name: Casey Summers
Estimated time: 50m
Actual time: 30m
"""

from prac_06.guitar import Guitar


def main():
    """Program to store a list of guitars and display class information."""
    print("My Guitars!")
    guitars = []

    name = input("Name: ")
    # name = "Fender Stratocaster"  # Test input
    while name != "":
        year = int(input("Year: "))
        # year = 2014  # Test input
        cost = float(input("Cost: $"))
        # cost = 765.4  # Test input
        # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))  # Test append
        # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))  # Test append
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input(f"\nName: ")

    print("\nThese are my guitars:")
    for guitar_num, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {guitar_num}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
