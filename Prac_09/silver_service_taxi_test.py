"""
CP1404/CP5632 Practical 09
silver_service_taxi test
"""

from Prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
    silver_taxi.drive(18)
    print(f"{silver_taxi}. The fare is ${silver_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
