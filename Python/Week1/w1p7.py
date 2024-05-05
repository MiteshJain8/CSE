# 7.	Write a python program to display all the prime numbers between a range

def dispPrimes(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

dispPrimes(20, 50)