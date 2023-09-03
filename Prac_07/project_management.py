"""
CP1404/CP5632 Practical 07
project_management.py
Theodore Lee
"""

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n")

def main():
    print(MENU)
    choice = input(">>> ").upper().strip()
    while choice != "Q":
        if choice == "L":
            print("load projects")
        elif choice == "S":
            print("save projects")
        elif choice == "D":
            print("display projects")
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