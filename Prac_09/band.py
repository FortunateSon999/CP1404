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
        musician_info = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_info})"

    def add(self, musician):
        """Adds a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        result = ""
        for musician in self.musicians:
            result += f"{musician.play()}\n"
        return result
