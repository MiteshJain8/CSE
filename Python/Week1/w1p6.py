# 6.	Write a Python program to display if the entered number is an Armstrong number or not

def isArmstrong(num):
    s = str(num)
    l = len(s)
    
    sumOfPows = sum(int(i) ** l for i in s)
    
    return sumOfPows == num

n = int(input("Enter a number: "))
if isArmstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")