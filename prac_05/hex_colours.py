"""
CP1404 Practical
Hex colours in CONSTANT dictionary
Name: Casey Summers
"""

TEN_COLOURS_TO_CODES = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff",
                        "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                        "Antique White0": "#faebd7", "Antique White1": "#ffefdb", "Antique White2": "#eedfcc"}

colour_choice = input("What colour: ").title().replace(" ", "")
while colour_choice != "":
    if colour_choice in TEN_COLOURS_TO_CODES:
        print(f"The colour code for {colour_choice} is: {TEN_COLOURS_TO_CODES[colour_choice]}")
    else:
        print("Invalid.")
    colour_choice = input("What colour: ").title()
print("Thank you for trying!")
