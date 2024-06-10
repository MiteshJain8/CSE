# Develop a python program to create a text file and ask the user to enter 5-6 lines of text. Display the total number of lines, characters and digits present in the file. Also display how many times a pecific word has appeared in the file

print("Enter 5 lines of text:")
lines = []
for i in range(5):
    line = input(f"Line {i+1}: ")
    lines.append(line)

word = input("Enter the word: ")

filename = "w6p3.txt"

with open(filename, "w") as file:
    for line in lines:
        file.write(line + "\n")

lineCount = 0
charCount = 0
digitCount = 0
wordCount = 0

with open(filename, "r") as file:
    for line in file:
        lineCount += 1
        charCount += len(line)
        digitCount += sum(1 for c in line if c.isdigit())
        wordCount += line.lower().split().count(word.lower())

print("\nDetails saved in the file:")
with open(filename, "r") as file:
    print(file.read())

print(f"No. of lines: {lineCount}")
print(f"No. of characters: {charCount}")
print(f"No. of digits: {digitCount}")
print(f"'{word}' appeared {wordCount} times")