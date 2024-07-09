# Develop a python program to create a text file and ask the user to enter 5-6 lines of text. Count the number of upper case, lower case and digits in the file. Display the details of the file

print("Enter 5 lines of text:")
lines = [input(f"Line {i+1}: ") for i in range(5)]

filename = "file1.txt"

with open(filename, "w") as file:
    for line in lines:
        file.write(line + "\n")

uppercase = 0
lowercase = 0
digit = 0

with open(filename, "r") as file:
    for line in file:
        for char in line:
            if char.isupper():
                uppercase += 1
            elif char.islower():
                lowercase += 1
            elif char.isdigit():
                digit += 1

print(f"\nNo. of uppercase letters: {uppercase}")
print(f"No. of lowercase letters: {lowercase}")
print(f"No. of digits: {digit}")

print("\nDetails:")
with open(filename, "r") as file:
    print(file.read())