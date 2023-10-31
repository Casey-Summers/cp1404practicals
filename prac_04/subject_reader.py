"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Shows example output then collects information into nested list that is later formatted."""
    data = get_data()
    print(data)  # display list output for function below
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    final_list = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        final_list.append(parts)
    input_file.close()
    return final_list


def display_subject_details(data):
    """Displays the nested list information in an f-string format."""
    counter = 0
    for person in data:
        print(f"{data[counter][0]} is taught by {data[counter][1]} and has {data[counter][2]} students")
        counter += 1


main()
