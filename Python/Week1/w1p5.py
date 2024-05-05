# 5.	Write a python program to display all the prime numbers within an interval using for loop

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

for num in range(start, end + 1):
    if is_prime(num):
        print(num)
