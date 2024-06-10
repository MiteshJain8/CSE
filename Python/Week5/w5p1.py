# Develop a python program to count all the occurrences of vowels, consonants and digits from the given text using Regular expressions.

import re

st = input("Enter the text:")
v = re.findall('[aeiouAEIOU]', st)
print("Vowel occurrences =",len(v))
print("Consonant occurrences =",len(st)-len(v))