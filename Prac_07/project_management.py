"""
CP1404/CP5632 Practical 07
project_management.py
Theodore Lee
That day is/was Sunday
03/09/2023 - 1530hrs
"""

#import datetime
from project import Project

# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))
FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n")


def main():
    print(MENU)
    projects = get_projects()
    choice = input(">>> ").upper().strip()
    while choice != "Q":
        if choice == "L":
            print("load projects")
        elif choice == "S":
            print("save projects")
        elif choice == "D":
            print("display projects")
            display_projects(projects)
        elif choice == "F":
            print("filter projects by date")
        elif choice == "A":
            print("add new project")
        elif choice == "U":
            print("update project")
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper().strip()


def get_projects():
    """Loads projects from file, and stores them in a list."""
    projects = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()

        for line in in_file:
            data = line.strip().split("\t")
            project = Project(data[0], data[1], data[2], data[3], data[4])
            projects.append(project)

        for project in projects:
            print(project)
    # Returns a list of objects
    return projects


def display_projects(projects):
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        # Checking if project is completed
        if int(project.completion_percentage) == 100:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
        sorted_complete_projects = sorted(complete_projects)
        sorted_incomplete_projects = sorted(incomplete_projects)
    print("Incomplete projects:")
    for project in sorted_incomplete_projects:
        print(f"\t{project}")
    print("Completed projects:")
    for project in sorted_complete_projects:
        print(f"\t{project}")


def update_project(projects):
    count = 0
    for project in projects:
        print(count, project)
        count += 1
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = int(input("New percentage: "))
    new_priority = int(input("New priority: "))
    projects[project_choice].priority = str(new_priority)
    projects[project_choice].completion_percentage = str(new_percentage)




if __name__ == "__main__":
    main()
