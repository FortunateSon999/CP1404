"""
CP1404/CP5632 Practical 09
silver_service_taxi
"""

from Prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A Silver Service Taxi that charges a premium fare."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness: float):
        # Code to inherit name and fuel from superclass.
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Now each object instance will be created with current_fare_distance initialized at 0.
        self.current_fare_distance = 0
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price of the trip."""
        return round(super().get_fare() + self.flagfall, 1)
