"""
CP1404/CP5632 Practical
State names in a dictionary NEW
"""

# Reformatting complete
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# print all state name with formatting
max_width = max(len(state) for state in CODE_TO_NAME)
for codes, states in CODE_TO_NAME.items():
    print(f"{codes:{max_width}} is {states} ")

# ask for state to validate and print
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper

    # LBYL approach
    # if state_code in CODE_TO_NAME:
    #     print(state_code, "is", CODE_TO_NAME[state_code])
    # else:
    #     print("Invalid short state")
    # state_code = input("Enter short state: ").upper()
