"""
CP1404 Practical 06 - guitars.py
Theodore Lee
"""

from Prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        if guitar.is_vintage():
            print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:.2f} (vintage) added.")
        else:
            print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:.2f} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == '__main__':
    main()
