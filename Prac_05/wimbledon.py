"""
CP1404/CP5632 Practical
wimbledon.py

Estimate: 30 minutes
Actual: 50 minutes
"""
FILENAME = "wimbledon.csv"

def read_data(filename):
    """Reads data from the files, and returns it as a list."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
    return lines[1:]  # Skip header

def get_champion_wins(data):
    """Takes data, and returns the champions and their wins."""
    champions = {}
    for line in data:
        line_list = line.strip().split(",")
        champion_name = line_list[2]
        if champion_name in champions:
            champions[champion_name] += 1
        else:
            champions[champion_name] = 1
    return champions

def get_countries(data):
    """Takes data and returns a set of countries that have championships."""
    countries = set()
    for line in data:
        line_list = line.strip().split(",")
        countries.add(line_list[1])
    return countries

def main():
    data = read_data(FILENAME)
    champion_wins = get_champion_wins(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for name, wins in champion_wins.items():
        print(f"{name} {wins}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    victor_countries = ", ".join(countries)
    print(victor_countries)


main()
