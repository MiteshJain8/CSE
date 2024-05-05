# 8.	Write a Python program to construct the following pattern, using a nested for loop
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

n = 5
for i in range(n):
    print (i*'* ')


for i in range(n,0,-1):
    print(i*'* ')