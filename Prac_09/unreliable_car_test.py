"""
CP1404/CP5632 Practical 09
UnreliableCar test
"""


from Prac_09.unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar("Toyota", 100, 50)
    print(f"{unreliable_car} drove {unreliable_car.drive(50)}km")
    print(f"{unreliable_car} drove {unreliable_car.drive(40)}km")


if __name__ == "__main__":
    main()
