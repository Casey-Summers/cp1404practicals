"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    camry = Car(180, "Camry")
    limo = Car(100, "Limo")
    camry.add_fuel(40)
    limo.add_fuel(20)
    print(f"{camry.name} has fuel: {camry.fuel}")
    print(f"{limo.name} has fuel: {limo.fuel}")
    camry.drive(75)
    limo.drive(115)
    print(camry)
    print(limo)


main()
