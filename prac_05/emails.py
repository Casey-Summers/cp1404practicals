"""
Email to name dictionary task
Estimate: 50 minutes
Actual:   62 minutes
Name: Casey Summers

Dodgy pseudocode to get an understanding of the task:

get user email
create dictionary
while email doesn't equal blank
    email.find '@' .split'.'
    is your name "NAME"
    if choice is Y
        add to dictionary
    elif choice is n
        print "Name: "
        add to dictionary
    print email
"""


def main():
    """Program that take an email address and prints it into a dictionary with an associated name."""
    user_email = input("Email: ")
    # user_email = 'Casey.summers@jcu.edu.au'  # Test value for email
    emails_to_names = {}
    while user_email != "":
        joined_name = extract_name(user_email)
        is_name_correct = input(f"Is your name {joined_name}? (Y/N): ").upper()
        if is_name_correct == 'Y' or is_name_correct == '':
            emails_to_names[joined_name] = user_email
        else:
            changed_name = input("Name: ")
            emails_to_names[changed_name] = user_email
        user_email = input("Email: ")
    print("")
    for names, emails in emails_to_names.items():
        print(f"{names} ({emails})")


def extract_name(user_email):
    """Reads the email until the index of the @ symbol and splits the name across a '.', then joining them."""
    split_name = (user_email[:user_email.find('@')]).split(".")
    joined_name = ' '.join(split_name).title()
    return joined_name


main()
