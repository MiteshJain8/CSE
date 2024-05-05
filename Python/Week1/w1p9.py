# 9.	Write a python program that asks the user to guess the lucky number. There will be five chances to guess the lucky number. Use a while loop and a counter. The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs "Good guess!", otherwise it outputs "Try again!". After the fifth guess it stops and prints "Game over."

import random

lucky_number = random.randint(1, 20)
guesses_taken = 0

while guesses_taken < 5:
    user_guess = int(input("Guess the lucky number: "))
    if user_guess == lucky_number:
        print("Good guess!")
    else:
        print("Try again!")
    guesses_taken += 1

print("Game over.")
