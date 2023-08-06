"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students and return nested list."""
    input_file = open(FILENAME)
    nested_list = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        nested_list.append(parts)
    input_file.close()
    return nested_list

def display_subject_details(nested_list):
    """Display subject details from nested list."""
    for subject_details in nested_list:
        print("{} is taught by {} and has {} students".format(*subject_details))


main()
