# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a python dictionary

def char_freq(str):
    freq = {}
    for char in str:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

str = input("Enter a string: ")
print(char_freq(str))