# Develop a python program to find all the urls in given string

import re

st = input("Enter a string:")
print(re.findall(r'(https?://(?:www\.)?[a-zA-Z0-9./?=&-_]+)', st))