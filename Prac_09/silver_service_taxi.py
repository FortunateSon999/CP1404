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
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fair, {self.price_per_km}/km "
                f"plus flagfall of {self.flagfall}")

    def get_fare(self):
        """Return the price of the trip."""
        return self.flagfall + (self.price_per_km * self.fanciness)
