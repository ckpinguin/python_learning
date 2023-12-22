from art import logo
import os
import random

finished = False

while not finished:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        number_of_attempts = 10
    elif difficulty == "hard":
        number_of_attempts = 5
    else:
        raise Exception("Invalid input.")

    print("I'm thinking of a number between 1 and 100.")
    rand_num = random.randint(1, 100)
    # Debug: print(f"Pssst, the correct answer is {rand_num}")

    while number_of_attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == rand_num:
            print(f"You got it! The answer was {rand_num} 🏆.")
            break
        elif guess > rand_num:
            print("Too high 🚀.")
        elif guess < rand_num:
            print("Too low 📉.")
        else:
            raise Exception("Invalid input.")
        number_of_attempts -= 1

        if number_of_attempts == 0:
            print("You've run out of guesses, you lose 🙀.")
            break
        print(
            f"You have {number_of_attempts} attempts remaining to guess the number.")
    more = input("Another round? (y/n): ").lower()
    if more == "n":
        finished = True
        print("Goodbye 👋.")
    elif more == "y":
        os.system("clear")
    else:
        raise Exception("Invalid input.")
