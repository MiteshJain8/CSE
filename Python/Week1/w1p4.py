def calculate_factorial(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial

num = int(input("Enter a number: "))

factorial = calculate_factorial(num)
print(f"The factorial of {num} is: {factorial}")
