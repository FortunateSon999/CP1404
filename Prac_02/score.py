"""
CP1404/CP5632 - Practical 2
Broken program to determine score status
"""


from random import randint


def main():
    """Takes score and prints grade."""
    score = float(input("Enter score: "))
    print(get_grade(score))
    random_score = randint(1, 100)
    print(get_grade(random_score))


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
