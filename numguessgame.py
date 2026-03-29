import random

# List of numbers given in the quiz
numbers = [1, 3, 5, 7, 9, 11, 13, 15]

print("Welcome to Harsh's Number Guessing Quiz!")
print("These are the numbers in the list:")
print(numbers)

# Judge chooses a random number from the list
secret_number = random.choice(numbers)

# Game loop
while True:
    guess = input("Guess the number the judge chose: ")

    # Validate input
    if not guess.isdigit():
        print("Please enter a valid whole number.")
        continue

    guess = int(guess)

    # Check if guess is in the list
    if guess not in numbers:
        print("Your guess must be from the list above.")
        continue

    # Compare guess with secret number
    if guess == secret_number:
        print("🎉 Correct! You guessed the judge's number!")
        break
    elif guess > secret_number:
        print("Your guess is HIGHER than the judge's number. Try again.")
    else:
        print("Your guess is LOWER than the judge's number. Try again.")
