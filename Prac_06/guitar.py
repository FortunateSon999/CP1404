"""
CP1404 Practical 06 - Guitar
Theodore Lee
"""


class Guitar:
    """Initialises a guitar instance."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return(f"{self.name} ({self.year}) : {self.cost}")

    def get_age(self):
        """Returns how old the guitar is in years."""
        return 2023 - self.year

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False
