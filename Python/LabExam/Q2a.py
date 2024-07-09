# Write a python program to display all the prime numbers in the given range

def displayPrimes(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

start = int(input("Enter start: "))
end = int(input("Enter end: "))
displayPrimes(start, end)