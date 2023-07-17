"""
CP1404/CP5632 - Practical
Loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for j in range(0, 100, 10):
    print(j, end = " ")
print()

# b.
for k in range(20, 0, -1):
    print(k, end = " ")
print("")

# c. 
n = int(input("Enter number of *: "))
for _ in range(0, n, 1):
    print("*", end = "")
print("")

# d.
for i in range(1, n + 1):
    print(i * "*")
