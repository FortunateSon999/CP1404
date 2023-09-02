"""
CP1404 Practical 07 - myguitars.py
Theodore Lee

Write a program to read all of these guitars and store them in a list of Guitar objects,
using the class that you wrote recently.
Display these using a loop.
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars_data = []
    guitar_objects = []
    with open(FILENAME, 'r', newline='') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars_data.append((name, year, cost))
            print(guitars_data)

        for name, year, cost in guitars_data:
            new_guitar = Guitar(name, year, cost)
            guitar_objects.append(new_guitar)

    for guitar in guitar_objects:
        print(guitar)


if __name__ == "__main__":
    main()
