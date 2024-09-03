import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)
guess = None

print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

# Loop until the user guesses the correct number
while guess != target_number:
    guess = int(input("Enter your guess: "))

    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

print("Thanks for playing!")