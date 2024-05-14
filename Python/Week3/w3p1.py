# Write a python program to create a tuple with random number find the Maximum and Minimum K elements in Tuple. 
# Input : test_t = (3, 7, 1, 18, 9), k = 2  
# Output : (3, 1, 9, 18) 
# Input : test_t = (3, 7, 1), k=1  
# Output : (1, 3) 

import random

def find_max_min_elements(test_t, k):
    sorted_t = sorted(test_t)
    return tuple(sorted_t[:k] + sorted_t[-k:])

n = int(input("Enter the number of elements in the tuple: "))
test_t = tuple(random.randint(1, 20) for i in range(n))
k = int(input("Enter the value of k: "))
print("Input Tuple:", test_t)
print("Output Tuple:", find_max_min_elements(test_t, k))