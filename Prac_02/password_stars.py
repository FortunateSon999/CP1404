"""Takes an entry and displays an equal length of stars."""


answer = input("Enter password: ")
while len(answer) <= 0:
    print("Invalid entry")
    answer = input("Enter password: ")
print("*" * len(answer))

