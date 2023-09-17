"""
CP1404/CP5632 Practical  09
Band class
"""

from musician import Musician


class Band:
    """A class band which contains musicians."""
    def __init__(self, name: str):
        """Constructs a band which has a name and consists of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({self.musicians[0]}{self.musicians[1]}{self.musicians[2]}{self.musicians[3]})"

    def add(self, musician):
        """Adds a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician.play())
2