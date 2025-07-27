import random

secret_number = random.randint(1, 10)
attempts = 3

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

while attempts > 0:
    guess = int(input("Take a guess: "))

    if guess == secret_number:
        if attempts == 3:
            print("Amazing! You guessed the number on your first try!")
        else:
            print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
    attempts -= 1

if attempts == 0:
    print("Sorry, you didn't make any attempts. The secret number was:", secret_number)