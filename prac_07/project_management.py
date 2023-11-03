"""
CP1404 - Project management program with several class, sorting, and saving functions.
Name: Casey Summers
Expected time: 90m
Actual time: 150m
"""

from project import Project
import csv
import datetime

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project " \
       "\n- (U)pdate project\n- (Q)uit\n"


def main():
    """Program with menu functions to save, load, filter, display and add projects based on .csv."""
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
            projects.sort()
            # Uses the __lt__ class def to sort by priority (ascending)
            print("Incomplete projects:")
            display_projects(projects, "<")
            print("Complete projects:")
            display_projects(projects, "==")
        elif choice == "F":
            filtered_projects = []
            start_date_filter = input("Show projects that start after date (dd/mm/yy): ")
            start_date_filter = datetime.datetime.strptime(start_date_filter, "%d/%m/%Y").date()

            for project in projects:
                project_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
                if project_date >= start_date_filter:
                    filtered_projects.append(project)

            # Sorts and prints filtered dates
            sorted_dates = sorted(filtered_projects)
            for date in sorted_dates:
                print(date)
        elif choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = input("Start Date (dd/mm/yy): ")
            priority = input("priority: ")
            cost = int(input("Cost estimate: $"))
            completion_percentage = int(input("Percent complete: "))
            projects.append(Project(name, start_date, priority, cost, completion_percentage))
        elif choice == "U":
            for i, project in enumerate(projects, 0):
                print(f"{i} {project}")
            project_choice = int(input("Project choice: "))
            print(projects[project_choice])
            new_completion = input("New Percentage: ")
            new_priority = input("New priority: ")
            projects[project_choice].completion_percentage = new_completion
            projects[project_choice].priority = new_priority
        else:
            print("Invalid input")
        choice = input(f"{MENU}>>> ").upper()
    print(f"Thank you for using custom-built project management software.")


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
    """Displays the object based on its completion using __str__ dunder method."""
    for project in projects:
        completion_percent = int(project.completion_percentage)
        # distinguishes between the two cases, either being "<" or "==" to 100% complete
        if (determinant == "<" and completion_percent < 100) or (determinant == "==" and completion_percent == 100):
            print(f"  {project}")


if __name__ == '__main__':
    main()
