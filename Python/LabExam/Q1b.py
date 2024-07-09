# Write a python program to create a list of tuples having first element as the strings and the second element as the length of the string. Output the list of tuples sorted based on the length of the string.

n = int(input("Enter the number of strings: "))
print("Enter the strings:")
strings = [input() for i in range(n)]
sorted_strings = sorted(strings, key=len)
tuples = []
for string in sorted_strings:
    tuples.append((string, len(string)))
print("Tuples:", tuples)