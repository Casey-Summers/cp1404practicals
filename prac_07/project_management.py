"""
CP1404 - Project management program with several class, sorting, and saving functions.
Name: Casey Summers
Expected time: 90m
Actual time:
"""

from project import Project
import csv

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project " \
       "\n- (U)pdate project\n- (Q)uit\n"


def main():
    choice = input(f"{MENU}>>> ").upper()
    projects = load_projects_from_csv(FILENAME)  # default load file encase user does not load a new one first
    while choice != "Q":
        if choice == "L":
            file_name = input("Filename: ")
            try:
                projects = load_projects_from_csv(file_name)
                # displays both incomplete and complete songs one after another
                display_projects(projects, "<")
                display_projects(projects, "==")
            except FileNotFoundError:
                print("That file does not exist.")
        elif choice == "S":
            file_name = input("Filename: ")
            save_projects_to_file(projects, file_name)
        elif choice == "D":
            # Uses the __lt__ class def to sort by priority (ascending)
            projects.sort()
            print("Incomplete projects:")
            display_projects(projects, "<")
            print("Complete projects:")
            display_projects(projects, "==")
        elif choice == "F":
            print("")
        elif choice == "A":
            print("")
        elif choice == "U":
            print("")
        else:
            print("Invalid input")
        choice = input(f"{MENU}>>> ").upper()
    print(f"Thank you for using custom-built project management software.")
    # save_projects_to_file(projects)


def load_projects_from_csv(filename):
    """Loads the .csv and sorts objects into list using Guitar class."""
    projects = []
    with open(filename, 'r') as in_file:
        csv_reader = csv.reader(in_file, delimiter='\t')
        in_file.readline()  # 'Consume' header for each column
        for row in csv_reader:
            try:
                name, start_date, priority, cost_estimate, completion_percentage = row
                guitar = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(guitar)
            except ValueError:
                print("Objects expected and objects present may not match.")
        return projects


def save_projects_to_file(projects, file_name):
    """Save lists of class objects back into the file with the same format."""
    with open(file_name, 'w') as out_file:
        for project in projects:
            out_file.write(f"{project.name},{project.start_date},{project.priority},{project.cost_estimate},"
                           f"{project.completion_percentage}\n")


def display_projects(projects, determinant):
    for project in projects:
        completion_percent = int(project.completion_percentage)
        # distinguishes between the two cases, either being "<" or "==" to 100% complete
        if (determinant == "<" and completion_percent < 100) or (determinant == "==" and completion_percent == 100):
            print(f"  {project}")


if __name__ == '__main__':
    main()
