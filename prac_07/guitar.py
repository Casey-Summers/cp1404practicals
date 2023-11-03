"""
Name: Casey Summers
CP1404 Practical - Guitar class.
"""

VINTAGE_THRESHOLD = 50
CURRENT_YEAR = 2023


class Guitar:
    """Class to gather guitar name, year, and cost, as well as get_age and check if it is vintage."""

    def __init__(self, name="", year=0.0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}), ${self.cost:,}"

    def __lt__(self, other):
        return self.year > other

    def get_age(self):
        """Gets age difference."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determines if a guitar is older than 50."""
        return self.get_age() >= VINTAGE_THRESHOLD
