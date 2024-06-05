# Develop a python program to find all three, four and five characters long word in a string

import re

st = input("Enter a string: ")
print("Three, four and five characters long words in the string are:")
print(re.findall(r'\b\w{3}\b', st))
print(re.findall(r'\b\w{4}\b', st))
print(re.findall(r'\b\w{5}\b', st))