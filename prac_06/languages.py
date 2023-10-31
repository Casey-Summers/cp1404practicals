"""
CP1404 Practical - Client code to use the ProgrammingLanguages class.
Name: Casey Summers
Estimated time: 35m
Actual time: 15m
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(f"{python}\n")  # Tests the __str__ method

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    dynamic_languages = [language.name for language in languages if language.is_dynamic()]
    print("\n".join(dynamic_languages))  # Saves a line over a conventional for loop


main()
