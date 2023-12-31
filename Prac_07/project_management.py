"""
CP1404/CP5632 Practical 07
project_management.py
Theodore Lee
That day is/was Sunday
03/09/2023
Start: 1530hrs
Finish: 2035hrs
Estimated time: 2 hours
Actual time: 5 hours
"""

import datetime
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
    projects = get_projects(FILENAME)
    choice = input(">>> ").upper().strip()
    while choice != "Q":
        if choice == "L":
            new_filename = input("Filename: ")
            projects = get_projects(new_filename)
        elif choice == "S":
            print("save projects")
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "D":
            print("display projects")
            display_projects(projects)
        elif choice == "F":
            print("filter projects by date")
            filter_by_date(projects)
        elif choice == "A":
            print("Let's add new project")
            new_project = get_new_project()
            projects.append(new_project)
        elif choice == "U":
            print("update project")
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper().strip()


def get_projects(filename):
    """Loads projects from file, and stores them in a list."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()

        for line in in_file:
            data = line.strip().split("\t")
            project = Project(data[0], data[1], data[2], data[3], data[4])
            projects.append(project)

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

    try:
        project_choice = int(input("Project choice: "))
        if project_choice < 0 or project_choice >= len(projects):
            print("Invalid project choice.")
            return
        new_percentage = int(input("New percentage: "))
        new_priority = int(input("New priority: "))
        if new_percentage < 0 or new_percentage > 100 or new_priority < 0:
            print("Invalid percentage or priority values.")
            return
    except ValueError:
        print("Invalid input. Please enter numbers for project choice, percentage, and priority.")
        return

    projects[project_choice].priority = str(new_priority)
    projects[project_choice].completion_percentage = str(new_percentage)


def get_new_project():
    """Gets the data for a new project and returns it."""
    try:
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yy): ")
        priority = int(input("Priority: "))
        cost = float(input("Cost estimate: $"))
        percentage_complete = int(input("Percent complete: "))

        if priority < 0 or cost < 0 or percentage_complete < 0 or percentage_complete > 100:
            print("Invalid input values. Priority, cost, and percentage must be positive values, "
                  "and percentage must be between 0 and 100.")
            return None
    except ValueError:
        print("Invalid input. Priority, cost, and percentage must be numbers.")
        return None

    new_project = Project(name, start_date, priority, cost, percentage_complete)
    return new_project


def filter_by_date(projects):
    """Filters projects by date."""
    filtered_date = []
    date_filter = input("Show projects that start after the date (dd/mm/yyyy): ")

    # Convert the input date string to a datetime object for comparison
    try:
        date_filter = datetime.datetime.strptime(date_filter, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    for project in projects:
        # Change the project's date into datetime object
        project_start_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y")

        # Compare the dates
        if project_start_date >= date_filter:
            filtered_date.append(project)

    if filtered_date:
        print("Projects starting after", date_filter.strftime("%d/%m/%Y"))
        for project in filtered_date:
            print(f"\t{project}")
    else:
        print("No projects found starting after", date_filter.strftime("%d/%m/%Y"))


def save_projects(filename, projects):
    """Saves projects to file."""
    with open(filename, 'w') as out_file:
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


if __name__ == "__main__":
    main()
