"""
CP1404 Practical - unreliable car child class
Expected: 25m
Actual:
"""

from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability float attribute."""
    price_per_km = 1.23

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with a reliability value."""
        return f"{super().__str__()}, reliability: {self.reliability}"

    def drive(self, distance):
        """Drive like parent Car but only if the random reliability is less than the objects."""
        distance_driven = super().drive(distance)
        if random.randint(0, 100) < self.reliability:
            return distance_driven
        else:
            "Your car broke down. Sorry."
