"""
CP1404 - SilverServiceTaxi class and client test
Name: Casey Summers
Expected: 40m
Actual: 55m
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Client program to test SilverServiceTaxi child class with fanciness attribute."""

    # Display Taxi class 'drive' and 'calculate_fare' functions
    silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
    silver_taxi.drive(18)  # Test drive value
    fare = silver_taxi.calculate_fare()
    print(f"A fare of {silver_taxi.current_fare_distance}km in a SilverServiceTaxi with fanciness of "
          f"{silver_taxi.fanciness} will cost: ${fare:.2f}")

    # Displaying taxi information
    print(f"\n{silver_taxi}")


if __name__ == "__main__":
    main()
