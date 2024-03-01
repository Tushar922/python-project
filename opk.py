import random

secret_number = random.randint(1, 100)


guesses = 10

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 10 chances to guess it.")

while guesses > 0:
    try:
        guess = int(input("Guess a number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue  

    guesses -= 1

    if guess == secret_number:
        print("Congratulations! You guessed the number in", 10 - guesses, "guesses!")
        break
    elif guess < secret_number:
        print("Too low! Try guessing a higher number.")
    else:
        print("Too high! Try guessing a lower number.")

if guesses == 0:
    print("Sorry, you ran out of guesses. The number was", secret_number)
