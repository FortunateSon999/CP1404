"""Testing class and inheritance."""

from datetime import datetime


class Person:
    """A person has a name and date of birth."""
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.name = name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        date_string = f"The current date is {datetime.now()}"

    def get_age(self):
        """Gets the persons age."""
        age = (datetime.now() - self.date_of_birth).date()
