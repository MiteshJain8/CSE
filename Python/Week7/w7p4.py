# Develop a python program to read the age of a person and display if he is eligible to vote or not. Raise the exception when the age range is less than 1 and greater than 150.

age = int(input("Enter your age: "))
if age < 1 or age > 150:
    raise Exception("Age must be between 1 and 150.")
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")