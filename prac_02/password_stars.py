"""Password to star converter"""

minimum_length = 3


def main():
    """Gets valid password and converts characters to asterisk"""
    password = get_password()
    print_password(password)


def print_password(password):
    """Gets valid password"""
    for character in range(len(password)):
        print("*", end="")


def get_password():
    """Uses valid password to print equal length of asterisks"""
    password = str(input("Password: "))
    while len(password) < minimum_length:
        print("Invalid password.")
        password = str(input("Password: "))
    return password


main()
