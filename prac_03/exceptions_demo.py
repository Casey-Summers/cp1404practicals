"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Q1. A ValueError will occur when the user enters a non-integer.
# Q2. A ZeroDivisionError will occur when the user enters '0' as the denominator.
# Q3. Yes. Either by checking for the error or by getting a valid input using a function.

# def main():
#     try:
#         numerator = int(input("Enter the numerator: "))
#         denominator = get_valid_denominator()
#         fraction = numerator / denominator
#         print(fraction)
#     except ValueError:
#         print("Numerator and denominator must be valid numbers!")
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")
#     print("Finished.")
#
#
# def get_valid_denominator():
#     denominator = int(input("Enter the denominator: "))
#     while denominator == 0:
#         print("Denominator cannot be 0.")
#         denominator = int(input("Enter the denominator: "))
#     return denominator
#
#
# main()
