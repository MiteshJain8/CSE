# Given a list of strings, write a Python program to create a list of tuples having first element as the string and second element as the length of the string. Output the list of tuples sorted based on the length of the string.

n = int(input("Enter the number of strings: "))
strings = []
for i in range(n):
    strings.append(input(f"Enter string {i+1}: "))

tuples = []
for string in strings:
    tuples.append((string, len(string)))

print("Tuples:", tuples)