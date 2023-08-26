"""
CP1404 Practical 06 - guitar_test.py
Theodore Lee
"""

from Prac_06.guitar import Guitar


def main():
    """Demo test code for guitar class."""
    my_guitar = Guitar("Gibson L-5 CES", 1923, 2000)
    another_guitar = Guitar("Another Guitar", 2013, 500)

    print(f"{my_guitar.name} get_age() - Expected 100. Got {my_guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age()}")
    print(f"{my_guitar.name} is_vintage() - Expected True. Got {my_guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


if __name__ == "__main__":
    main()
