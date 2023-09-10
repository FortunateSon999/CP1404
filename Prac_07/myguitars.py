"""
CP1404 Practical 07 - myguitars.py
Theodore Lee
"""

from guitar import Guitar

FILENAME = "guitars.csv"


from guitar import Guitar


def main():
    # Load existing guitars from the CSV file
    existing_guitars = load_existing_guitars()

    # Display the existing guitars
    display_guitars(existing_guitars)

    # Sort the existing guitars
    sorted_guitars = sorted(existing_guitars)
    print("Sorted guitars:")
    display_guitars(sorted_guitars)

    # Add new guitars
    add_new_guitars(existing_guitars)

    # Save all guitars back to the CSV file
    save_guitars_to_csv(existing_guitars)

def load_existing_guitars():
    """Load existing guitars from CSV file."""
    guitars_data = []
    with open(FILENAME, 'r', newline='') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars_data.append((name, year, cost))
    return [Guitar(name, year, cost) for name, year, cost in guitars_data]

def display_guitars(guitars):
    """Display guitars."""
    for guitar in guitars:
        print(guitar)


def add_new_guitars(existing_guitars):
    """Add new guitars to the existing_guitars list."""
    guitars_to_add = []
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars_to_add.append(guitar)
        if guitar.is_vintage():
            print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:.2f} (vintage) added.")
        else:
            print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:.2f} added.")
    existing_guitars.extend(guitars_to_add)


def save_guitars_to_csv(guitars):
    """Save guitars to CSV file."""
    with open(FILENAME, 'w', newline='') as out_file:
        for guitar in guitars:
            print(guitar, file=out_file)


if __name__ == "__main__":
    main()
