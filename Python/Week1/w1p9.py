# 9.	Write a python program that asks the user to guess the lucky number. There will be five chances to guess the lucky number. Use a while loop and a counter. The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs "Good guess!", otherwise it outputs "Try again!". After the fifth guess it stops and prints "Game over."

import random

guesses = 0
while guesses < 5:
    lucky_number = random.randint(1, 5)
    user_guess = int(input("Guess the number between 1 to 5: "))
    if user_guess == lucky_number:
        print("Good guess!")
    else:
        print("Try again!")
    guesses += 1

print("Game over.")