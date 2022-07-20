import random


def guessing_game():
    number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "hard":
        lives = 5
    else:
        lives = 10

    run_game = True

    while run_game:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("You win!")
            print(f"The Number was {number}!")
            run_game = False
        elif lives > 0:
            print("You lose!")
            run_game = False
        elif number > guess:
            print("Too low.")
            print("Guess again.")
            lives -= 1
        elif number < guess:
            print("Too high.")
            print("Guess again.")
            lives -= 1


guessing_game()
