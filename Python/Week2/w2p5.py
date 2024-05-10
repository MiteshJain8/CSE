# 5.	Create a displayFibonacci() function that displays the Fibonacci series between 0 to 100

def displayFibonacci():
    a, b = 0, 1
    while a <= 100:
        print(a, end=' ')
        a, b = b, a+b

displayFibonacci()