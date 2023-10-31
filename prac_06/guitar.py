"""
Name: Casey Summers
CP1404 Practical - Guitar class.
"""

VINTAGE_THRESHOLD = 50
CURRENT_YEAR = 2023


class Guitar:
    def __init__(self, name="", year=0.0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,}"

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        if self.year >= VINTAGE_THRESHOLD:
            return True
