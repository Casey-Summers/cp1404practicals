"""
CP1404 - Band class for my_band.py test program
Expected: 30m
Actual: 50m
"""


class Band:
    def __init__(self, band_type):
        self.band_type = band_type
        self.musicians = []

    def __str__(self):
        musician_str = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.band_type} ({musician_str})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        result = ""
        for musician in self.musicians:
            if not musician.instruments:
                result += f"{musician.name} needs an instrument!\n"
            else:
                result += f"{musician.name} is playing: {musician.instruments[0]}\n"
        return result
