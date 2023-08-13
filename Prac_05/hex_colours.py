"""
CP1404/CP5632 Practical
hex_colours.py
"""

COLOR_DICTIONARY = {"Alice Blue": "#f0f8ff", "Antique White": "#faebd7", "Antique White1": "#ffefdb",
                    "Antique White2": "#eedfcc", "Antique White3": "#cdc0b0", "Antique White4": "#8b8378",
                    "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amber1": "#ffbf00", "Amber2": "#eead0e"}
color_name = input("Enter color name: ").title()
while color_name != "":
    try:
        print(color_name, "is", COLOR_DICTIONARY[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").title()