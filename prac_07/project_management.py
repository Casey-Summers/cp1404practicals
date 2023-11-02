"""
CP1404 - Project management program with several class, sorting, and saving functions.
Name: Casey Summers
Expected time: 90m
Actual time:
"""

from project import Project
import csv

FILENAME = "projects.txt"


def main():
    projects = load_projects_from_csv(FILENAME)
    print(projects)


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


def save_projects_to_file(projects):
    """Save lists of class objects back into the file with the same format."""
    with open(FILENAME, 'w') as out_file:
        for project in projects:
            out_file.write(f"{project.name},{project.year},{project.cost}\n")


if __name__ == '__main__':
    main()
