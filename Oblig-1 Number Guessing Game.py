import random


numberMin = 0
numberMax = 100
maxAttempts = 5
attempts = 0

randomNumber = random.randint(numberMin, numberMax)


while True:
    guess = int (input("Type a number between 0 - 100: "))
    attempts += 1
        
    if guess < randomNumber:
        print("The number is bigger than your number")
        
    elif guess > randomNumber:
        print("The number is smaller than your number")
        
    elif guess == randomNumber:
        print(f"Congratulations! You guessed the number in {attempts} attempt(s).!")
        attempts = 0
        
    if attempts == maxAttempts:
        print("Sorry! You did not manage to guess the number. You have reached the guessing limit.")
        print(f"The number was: {randomNumber}")
        break
        



