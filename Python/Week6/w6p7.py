# Develop a python program to create 2 text files "file1.txt" and "file2.txt". Enter 10 random numbers in both of these files. Sort and merge the numbers from these two files and store it in a 3rd file named "Result.txt". Display the details of these files

import random

def write(filename):
    with open(filename, "w") as file:
        numbers = [random.randint(1, 100) for _ in range(10)]
        for num in numbers:
            file.write(f"{num}\n")

def read(filename):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]

write("file1.txt")
write("file2.txt")

lst1 = read("file1.txt")
lst2 = read("file2.txt")

lst3 = sorted(lst1 + lst2)

with open("Result.txt", "w") as file:
    for num in lst3:
        file.write(f"{num}\n")

print("\nfile1.txt:")
with open("file1.txt", "r") as file:
    print(file.read())

print("file2.txt:")
with open("file2.txt", "r") as file:
    print(file.read())

print("Result.txt:")
with open("Result.txt", "r") as file:
    print(file.read())