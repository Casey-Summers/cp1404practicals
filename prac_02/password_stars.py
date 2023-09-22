"""Password to star converter"""

minimum_length = 3


def main():
    password = get_password()
    print_password(password)


def print_password(password):
    for character in range(len(password)):
        print("*", end="")


def get_password():
    password = str(input("Password: "))
    while len(password) < minimum_length:
        print("Invalid password.")
        password = str(input("Password: "))
    return password


main()
