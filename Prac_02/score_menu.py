"""
CP1404 - Prac_02
Theodore Lee
"""


MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Displays menu, gets valid input and performs actions."""
    score = get_valid_score()
    print(MENU)
    user_choice = input("Input Choice: ").strip().upper()
    while user_choice != "Q":
        if user_choice == "G":
            score = get_valid_score()
        elif user_choice == "P":
            grade = get_grade(score)
            print(grade)
        elif user_choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        user_choice = input("Input Choice: ").strip().upper()
    print("Goodbye.")


def get_valid_score():
    """Asks user for a valid score, and returns it."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def get_grade(score):
    """Takes a score and returns the grade."""
    if score < 0:
        return "Invalid score"
    else:
        if score < 50:
            return "Bad"
        elif score < 90:
            return "Passable"
        else:
            return "Excellent"


main()
