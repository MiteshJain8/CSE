# Develop a python program to create a text file and ask the user to enter 5-6 lines of text. Display the longest and the shortest word from the file. Display the length of these words

print("Enter 5 lines of text:")
lines = [input(f"Line {i+1}: ") for i in range(5)]

filename = "file1.txt"

with open(filename, "w") as file:
    for line in lines:
        file.write(line + "\n")

with open(filename, "r") as file:
    longest = file.readline().split()[0]
    shortest = longest
    for line in file:
        words = line.split()
        for word in words:
            if len(word) > len(longest):
                longest = word
            if shortest is None or len(word) < len(shortest):
                shortest = word

print(f"\nLongest word: {longest} (Length: {len(longest)})")
print(f"Shortest word: {shortest} (Length: {len(shortest)})")