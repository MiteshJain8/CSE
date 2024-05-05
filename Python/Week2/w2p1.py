# 1.	Create a function sum() and a function multiply() that takes a list of numbers and  displays the sum of all the numbers if sum() is called and displays multiplication of all the numbers if the multiply() is called. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24

def mul(list):
    pro=1
    k = len(list)
    for i in range(k):
        pro*=list[i]
    return pro

n = int(input("Enter number of elements: "))
list = []
print("Enter the ",n," elements:")
for i in range(n):
    x = int(input())
    list.append(x)
print("Sum = ",sum(list))
print("Product = ",mul(list))