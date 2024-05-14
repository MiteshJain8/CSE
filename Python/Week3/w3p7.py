# a) Write a Python program to generate random even integers in a specific numerical range using the random module 
# b) Write a Python program to get a single random element from a specified string using the random module. 
# c) Write a Python program to generate a series of unique random numbers without any duplicates using the random module

import random

def random_even(start, end):
    while True:
        k = random.randrange(start, end)
        if(k%2==0):
            return k

def random_char(s):
    return random.choice(s)

def random_unique_nums(start, end, count):
    return random.sample(range(start, end), count)

print(random_even(10, 100))
print(random_char("Namaste, Duniya!"))
print(random_unique_nums(1, 100, 5))