"""
CP1404/CP5632 Practical  09
Taxi simulator
"""

from Prac_09.taxi import Taxi
from Prac_09.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    chosen_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    driven_taxis = []
    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").strip().lower()
    while user_choice != "q":
        if user_choice == "c":
            print("Taxis available:")
            chosen_taxi = choose_taxi(taxis)
        elif user_choice == "d":
            if chosen_taxi is not None:
                distance = int(input("Drive how far? "))
                chosen_taxi.drive(distance)
                print(f"Your {chosen_taxi.name} trip cost you ${chosen_taxi.get_fare():.2f}")
                driven_taxis.append(chosen_taxi)
            else:
                print("You need a chosen taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${get_total_bill(driven_taxis):.2f}")
        print(MENU)
        user_choice = input(">>> ").strip().lower()


def get_total_bill(driven_taxis):
    """Returns the current total taxi bill."""
    total_bill = 0
    for taxi in driven_taxis:
        total_bill += taxi.get_fare()
    return total_bill


def choose_taxi(taxis):
    "Gets a taxi."
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    taxi_choice = int(input("Choose taxi: "))
    try:
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
        return None


if __name__ == "__main__":
    main()
