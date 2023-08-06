"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    denominator = int(input("Enter the denominator: "))
print("Finished.")

# When will a ValueError occur?
# It will occur when the int() function attempts to convert a string into an integer.

# When will a ZeroDivisionError occur?
# It occurs when the denominator is assigned 0.

# Could you change the code to avoid the possibility of a ZeroDivisionError?