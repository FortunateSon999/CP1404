"""
CP1404/CP5632 Practical
Quick Picks
"""
import random


def main():
    number_of_picks = int(input("How many quick picks? "))
    lines = get_quick_pick(number_of_picks)

    # Display each quick pick
    for line in lines:
        print(" ".join("{:2}".format(num) for num in line))


def get_quick_pick(number_of_picks):
    """Get quick pick numbers."""
    nested_line = []
    for i in range(number_of_picks):
        line = []
        while len(line) < 6:
            random_number = random.randint(1, 45)
            if random_number not in line:
                line.append(random_number)
        line.sort()
        nested_line.append(line)
    return nested_line


main()
