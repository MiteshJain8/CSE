# Develop a python program to create a text file and ask the user to enter 5-6 lines of text. Display the total number of vowels and white spaces present in the files. Replace all the occurrences of a specific word from the file with the new word. Replace all the white spaces from the file with "_"

print("Enter 5 lines of text:")
lines = []
for i in range(5):
    line = input(f"Line {i+1}: ")
    lines.append(line)

word = input("Enter the word to replace: ")
newWord = input("Enter the new word: ")

filename = "w6p4.txt"

with open(filename, "w") as file:
    for line in lines:
        file.write(line + "\n")

vowelCount = 0
whitespaceCount = 0

with open(filename, "r") as file:
    content = file.read()
    vowelCount = sum(1 for c in content if c.lower() in 'aeiou')
    whitespaceCount = content.count(' ')
    content = content.replace(word, newWord)
    content = content.replace(' ', '_')

with open(filename, "w") as file:
    file.write(content)

print("\nModified content:")
with open(filename, "r") as file:
    print(file.read())

print(f"No. of vowels: {vowelCount}")
print(f"No. of white spaces: {whitespaceCount}")