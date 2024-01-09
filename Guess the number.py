import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of guesses
attempts = 0

print("Welcome to the Guessing Game!")

while True:
    # Ask the user for a guess
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the correct number ({secret_number}) in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
