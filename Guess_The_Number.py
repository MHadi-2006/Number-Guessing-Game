# I am gonna create a game for the uer to guess the number perfectly.

from random import randint

cpu = randint(1,100)

attempt = 0
n = -1

while n<attempt:
    user = int(input("Enter your guess : "))

    if user == cpu:
        print(f"Perfect Guess! Your total attempts were {attempt}.")

    elif user > cpu:
        print("Lower number please!")

    elif user < cpu:
        print("Higher number please!")

    attempt += 1

