"""
CP1404/CP5632 Practical
emails.py
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""


def main():
    emails_and_names = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        name = check_name(name)
        emails_and_names[name] = email
        email = input("Email: ")
    for name in emails_and_names:
        print(f"{name} ({emails_and_names[name]})")


def get_name(email):
    """Takes an email and returns the name."""
    test_list = email.split("@")
    name_part = test_list[0]  # Get the first element, which is the name part
    name = name_part.replace(".", " ").title()
    return name

def check_name(name):
    """Checks with the user if name is correct, and gets correct name if not."""
    print(f"Is your name {name}? (Y/n)", end="")
    answer = input("").lower()
    if answer == "" or answer == "y":
        return name
    else:
        corrected_name = input("Name: ")
        return corrected_name


main()
