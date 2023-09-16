"""
CP1404/CP5632 Practical 09
UnreliableCar class
"""

from car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability: float):
        """Initialise an unreliable car instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}"

    def drive(self, distance):
        """Drives the car a certain distance if it is reliable."""
        if randint(1, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven
