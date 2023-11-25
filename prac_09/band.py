"""
CP1404 - Band class for my_band.py test program
Expected: 30m
Actual: 50m
"""


class Band:
    """Represent a Band object consisting of musicians, music type, and instruments."""

    def __init__(self, band_type):
        """Initialise a Band instance with band type and musicals."""
        self.band_type = band_type
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band object."""
        musician_str = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.band_type} ({musician_str})"

    def add(self, musician):
        """Add a musicians to a 'musicals' list using the Class."""
        self.musicians.append(musician)

    def play(self):
        """Returns the talents of all musicians and their instruments using the list."""
        result = ""
        for musician in self.musicians:
            if not musician.instruments:
                result += f"{musician.name} needs an instrument!\n"
            else:
                result += f"{musician.name} is playing: {musician.instruments[0]}\n"
        return result
