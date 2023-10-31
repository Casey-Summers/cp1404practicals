"""
CP1404/CP5632 - Practical
Practise writing into files
"""

FILENAME = "name.txt"
FILENAME_2 = "numbers.txt"
MAX_INDEX = 3  # Choose which line you would like to read until

# Q1.
name = input("Name: ")
with open(FILENAME, "w") as in_file:
    in_file.write(name)

# Q2.
with open(FILENAME, "r") as in_file:  # "as if it were a separate program"
    name = in_file.readline()
    print(f"{name} has been written into {FILENAME}")

# Q3.
with open(FILENAME_2, "r") as in_file:
    number_one = in_file.readline()
    number_two = in_file.readline(2)
    total = int(number_one) + int(number_two)
    print(total)

# Q4.
with open(FILENAME_2, "r") as in_file:
    total = 0  # Clearing total back to zero.
    lines_read = 0
    while lines_read != MAX_INDEX:  # Breaks once the lines read equals the max index depth.
        for line in in_file:
            total += int(line)
            lines_read += 1
    print(total)
