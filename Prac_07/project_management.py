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
    projects = []
    with open(FILENAME, 'r') as in_file:
        for project in in_file:
            extracted_project = Project(project.strip().split("	"))
            projects.append(extracted_project)
        for project in projects:
            print(project)
    choice = input(">>> ").upper().strip()
    while choice != "Q":
        if choice == "L":
            print("load projects")
        elif choice == "S":
            print("save projects")
        elif choice == "D":
            print("display projects")
            with open(FILENAME, 'r') as in_file:
                for project in in_file:
                    if project[-1] != 100:
                        print(project)
        elif choice == "F":
            print("filter projects by date")
        elif choice == "A":
            print("add new project")
        elif choice == "U":
            print("update project")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper().strip()


if __name__ == "__main__":
    main()