# Develop a python program to read a C-program and display all the keywords. Display the keywords and their locations. Search for the "int, float, while, for, if, if else, else, switch, printf and scanf" keywords in the program

import re

keywords = ["int", "float", "while", "for", "if", "else if", "else", "switch", "printf", "scanf"]
C_prog = input("Enter the C program:")
pos = {}
for key in keywords:
    pos[key] = [m.start() for m in re.finditer(key, C_prog)]
print(pos)