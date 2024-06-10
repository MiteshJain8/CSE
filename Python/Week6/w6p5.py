# Develop a python program to create a text file and ask the user to enter 10 lines of text. Display the file in the reverse order. Display the 2nd and 3rd lines of the file. Display last 2 lines of the file

print("Enter 10 lines of text:")
lines = []
for i in range(10):
    line = input(f"Line {i+1}: ")
    lines.append(line)

filename = "w6p5.txt"

with open(filename, "w") as file:
    for line in lines:
        file.write(line + "\n")

with open(filename, "r") as file:
    fileLines = file.readlines()

print("\nFile content in reverse order:")
for line in reversed(fileLines):
    print(line.strip())

if len(fileLines) >= 3:
    print("\n2nd and 3rd lines of the file:")
    print(fileLines[1].strip())
    print(fileLines[2].strip())
else:
    print("\nFile has less than 3 lines.")

if len(fileLines) >= 2:
    print("\nLast 2 lines of the file:")
    print(fileLines[-2].strip())
    print(fileLines[-1].strip())
else:
    print("\nFile has less than 2 lines.")