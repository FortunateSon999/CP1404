"""
CP1404/CP5632 Practical  09
Taxi simulator
"""

from Prac_09.taxi import Taxi
from Prac_09.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!\n", MENU)
    user_choice = input(">>>").strip().lower()
    while user_choice != "q":
        for taxi in taxis:
            total_bill += taxi.get_fare()
        if user_choice == "c":
            print("choose taxi")
            chosen_taxi = choose_taxi(taxis)
            print()
        elif user_choice == "d":
            print("drive")
        else:
            print("Invalid choice")
        print(f"Bill to date: {total_bill}")
        print(MENU)
        user_choice = input(">>>").strip().lower()


def choose_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    taxi_choice = int(input("Choose taxi: "))
    try:
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")



if __name__ == "__main__":
    main()
