"""
CP1404/CP5632 - Practical
Standard menu design
"""


MENU = """(H)ello\n(G)oodbye\n(Q)uit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello Guido")
    elif choice == "G":
        print("Goodbye Guido")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
