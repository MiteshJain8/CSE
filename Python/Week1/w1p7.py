# 7.	Write a python program to display all the prime numbers between a range

def display_primes(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

display_primes(10, 50)