# 6.	Write a Python program to display if the entered number is an Armstrong number or not

def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    
    return sum_of_powers == num

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
