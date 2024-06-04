# Develop a python program to match all the occurrences of a word which has an "A/a" followed by  
# i. Zero or more b's
# ii. Zero or one b 
# iii. One and more b's 
# iv. Four consecutive b's followed by a “c”

import re

text = input("Enter the text: ")

print("'A' or 'a' followed by zero or more 'b's:",re.findall('[aA][bB]*', text))
print("'A' or 'a' followed by zero or one 'b':",re.findall('[aA][bB]?', text))
print("'A' or 'a' followed by one or more 'b's:",re.findall('[aA][bB]+', text))
print("'A' or 'a' followed by four 'b's followed by 'c':",re.findall('[aA][bB]{4}[cC]', text))