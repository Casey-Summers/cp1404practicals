"""
Name: Casey Summers
CP1404 Practical - Programming Languages class.
"""


class ProgrammingLanguage:
    """Class to gather name, typing, reflection, and year of a programming language, and to check if it is dynamic."""
    def __init__(self, name="", typing="", reflection=False, year=0.0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
