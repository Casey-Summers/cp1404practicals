"""
CP1404/CP5632 - Practical
Broken (now fixed) program to determine score status
"""


def main():
    """Takes a score and determines a grade."""
    score = get_valid_score()
    grade = determine_grade(score)
    print(f"Your grade is: {grade}")


def get_valid_score():
    """Repeats until a valid score is given."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
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


main()
