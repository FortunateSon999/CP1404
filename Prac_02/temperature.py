"""
CP1404/CP5632 - Practical 2
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Takes user input and converts temperature measurements."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            display_in_fahrenheit(celsius)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            display_in_celsius(fahrenheit)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def display_in_celsius(fahrenheit):
    """Takes temperature in Fahrenheit and displays it in Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Results: {celsius:.2f} C")


def display_in_fahrenheit(celsius):
    """Takes temperature in Celsius and displays it in Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")