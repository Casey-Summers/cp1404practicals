"""
CP1404 - Quick Pick Lottery ticket generator
Name: Casey Summers
"""

from random import randint

LOWER_RANDOM = 1
UPPER_RANDOM = 45
NUM_QUICK_PICKS = 5
NUM_PER_QUICK_PICK = 6


def main():
    """Program to generate lines of 6 random numbers equal to user request."""
    number_of_picks = int(input("How many quick picks? "))
    for picks in range(number_of_picks):
        line_of_quick_picks = generate_quick_pick_line()
        for pick_number in line_of_quick_picks:
            print(f"{pick_number:2}", end=" ")
        print()


def generate_quick_pick_line():
    """Generate a list with sorted quick picks without repeating numbers."""
    quick_pick = []
    while len(quick_pick) < NUM_PER_QUICK_PICK:
        num = randint(LOWER_RANDOM, UPPER_RANDOM)
        if num not in quick_pick:
            quick_pick.append(num)
    return sorted(quick_pick)


main()
