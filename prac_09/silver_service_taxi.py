"""
CP1404 Practical - SilverServiceTaxi child of Taxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes premium fare costs."""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness  # Adjust price_per_km based on fanciness

    def __str__(self):
        """Return a string like a Taxi but with a fanciness value."""
        return f"{super().__str__()} plus flagfall of ${self.flag_fall:.2f}"

    def calculate_fare(self):
        """Return the trip price like a Taxi but with a flag_fall fee."""
        base_fare = super().get_fare()
        return base_fare + self.flag_fall
