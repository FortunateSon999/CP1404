"""
CP1404/CP5632 Practical 09
taxi test
"""

from Prac_09.taxi import Taxi


def main():
    new_taxi = Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print(f"{new_taxi} Price: ${new_taxi.get_fare()}")
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(f"{new_taxi} Price: ${new_taxi.get_fare()}")


if __name__ == "__main__":
    main()
