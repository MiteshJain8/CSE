# Develop a python program to search word in a string and display the location within the original string where the pattern occurs. If the pattern occurs multiple times, then display all the locations. Replace the pattern with another word

import re

st = "program to search word. If word occurs many times, find all occurrence of word and also replace the word"
pat = "word"
locations = [m.start() for m in re.finditer(pat, st)]
print("Locations:",locations)
replace = "symbol"
st2 = re.sub(pat, replace, st)
print("After replacing:",st2)