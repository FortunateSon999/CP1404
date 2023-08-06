"""CP1404 Practical 3 - files.py"""

name = input("Enter your name: ")

with open("name.txt", "w") as file:
    file.write(name)

with open("name.txt", "r") as file:
    name = file.read()
    print(f"Your name is {name}")

with open("numbers.txt", "r") as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
    total = num1 + num2
    print(total)

total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        total += number

print(total)
