# 4.	Write a python program to find the factorial of number using while loop

def calcFact(num):
    fact = 1
    while num > 1:
        fact *= num
        num -= 1
    return fact

num = int(input("Enter a number: "))
fact = calcFact(num)
print(f"The factorial of {num} is: {fact}")