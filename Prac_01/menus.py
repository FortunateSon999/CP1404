"""
CP1404/CP5632 - Practical
Menus
"""
import pandas as pd



MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ").upper() 
print(MENU)
user_choice = input(">>> ").upper()

while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello {name}")
    elif user_choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid Choice")
    print(MENU)
    user_choice = input(">>> ").upper()

print("Finished.")
