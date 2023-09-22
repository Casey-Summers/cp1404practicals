"""
CP1404/CP5632 - Practical
Score menu program that follows standards structure with several functions
"""

MENU = "(G)et a valid score\n" \
       "(P)rint result\n" \
       "(S)how stars\n" \
       "(Q)uit"


def main():
    """Program with main menu to pick between different functions using a score value."""
    score = get_valid_score()
    print(MENU)
    choice = str(input("Choice: ")).upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            grade = determine_grade(score)
            print(f"Your score is: {grade}")
        elif choice == 'S':
            print_stars(score)
        choice = str(input("Choice: ")).upper()
    print("Thank you!")


def get_valid_score():
    """Gets valid score between 1-100."""
    score = int(input("Score (1-100): "))
    while score < 1 or score > 100:
        print("Invalid score.")
        score = int(input("Score: "))
    return score


def determine_grade(score):
    """Determines grade using score and score thresholds."""
    if score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade


def print_stars(score):
    """Prints length of stars equal to score int value."""
    for character in range(score):
        print("*", end="")
    print("")


main()
