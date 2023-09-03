"""
CP1404/CP5632 - Practical 07
project.py
Theodore Lee
"""


class Project:
    """Initialises a project instance."""
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return(f"{self.name},{self.start_date},{self.priority},{self.cost_estimate},{self.completion_percentage}")

    def __lt__(self, other):
        """Returns True if self's priority is less than other's priority, False otherwise."""
        return self.priority < other.priority

    def is_started_later(self, other):
        return self.start_date < other.start_date
