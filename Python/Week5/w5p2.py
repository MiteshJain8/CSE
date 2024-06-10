# Develop a python program to match all the occurrences of a word which has an "A/a" followed by  
# i. Zero or more b's
# ii. Zero or one b 
# iii. One and more b's 
# iv. Four consecutive b's followed by a “c”

import re

text = input("Enter the text: ")
print("'A/a' followed by:")
print("Zero or more 'b's:",re.findall('[aA][b]*', text))
print("Zero or one 'b':",re.findall('[aA][b]?', text))
print("One or more 'b's:",re.findall('[aA][b]+', text))
print("Four 'b's followed by 'c':",re.findall('[aA][b]{4}[c]', text))