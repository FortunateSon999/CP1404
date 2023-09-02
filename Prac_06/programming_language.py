class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initializes a programming language and its details."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing}, {self.reflection}, {self.year}"

    def is_dynamic(self):
        """Returns True or False depending on if a language is dynamically typed."""
        return self.typing == "Dynamic"

