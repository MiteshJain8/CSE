# Create a dictionary for words and their meanings. Write functions to add a new entry (word:meaning), search for a particular word and retrieve meaning, given meaning find words with same meaning, remove an entry, display all words sorted alphabetically. [Program must be menu driven]

dictionary = {}

def add_entry(word, meaning):
    dictionary[word] = meaning

def search_word(word):
    return dictionary.get(word, "Word not found in dictionary")

def find_words(meaning):
    words = []
    for key,value in dictionary.items():
        if value == meaning:
            words.append(key)
    return words

def remove_entry(word):
    if word in dictionary:
        del dictionary[word]
    else:
        return "Word not found in dictionary"

def display_words():
    for word in sorted(dictionary):
        print(f"{word}: {dictionary[word]}")

print("\n1. Add entry")
print("2. Search word")
print("3. Find words with same meaning")
print("4. Remove entry")
print("5. Display all words")
print("6. Exit")

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        word = input("Enter word: ")
        meaning = input("Enter meaning: ")
        add_entry(word, meaning)
    elif choice == 2:
        word = input("Enter word: ")
        print(search_word(word))
    elif choice == 3:
        meaning = input("Enter meaning: ")
        print(find_words(meaning))
    elif choice == 4:
        word = input("Enter word: ")
        print(remove_entry(word))
    elif choice == 5:
        display_words()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")