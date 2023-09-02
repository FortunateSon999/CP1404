"""Takes an entry and displays an equal length of stars."""


def main():
    """Takes an entry and displays an equal length of stars."""
    answer = get_password()
    display_stars(answer)


def display_stars(answer):
    print("*" * len(answer))


def get_password():
    answer = input("Enter password: ")
    while len(answer) <= 0:
        print("Invalid entry")
        answer = input("Enter password: ")
    return answer


main()
