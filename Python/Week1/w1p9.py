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
