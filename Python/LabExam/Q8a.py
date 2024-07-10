# Develop a python program to read 20 random numbers. Display all the odd numbers from this list which are of length 2 and 4.

print("Enter 20 random numbers: ")
nums = [int(input()) for i in range(20)]
oddNums = [num for num in nums if num % 2 != 0]
len2And4 = [num for num in oddNums if len(str(num)) in [2, 4]]
print(len2And4)