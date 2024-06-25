# Write an interactive program to compute the square root of a number. The input values must be tested for validity. If it is negative, the user defined method MySqrt() should raise an exception

def mySqrt(num):
    if num < 0:
        raise Exception("Cannot compute square root of a negative number.")
    else:
        print(num**0.5)

num = float(input("Enter a number: "))
mySqrt(num)