"""
CP1404/CP5632 - Practical 2
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    else:
        print("Excellent")
