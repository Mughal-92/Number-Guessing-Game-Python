import random


numberMin = 0
numberMax = 100
maxAttempts = 5
attempts = 0
playAgain = "y"
continueGame = True

randomNumber = random.randint(numberMin, numberMax)

def playAgain():
    global continueGame
    global randomNumber
    global attempts
    playAgain = input("Do you want to play again? (y/n): ")
    if playAgain == "y":
        randomNumber = random.randint(numberMin, numberMax)
        attempts = 0
        continueGame = True
    else:
        continueGame = False

while continueGame:
    guess = (input("Type a number between 0 - 100: "))
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a valid integer.")
        continue
    attempts += 1
        
    if guess < randomNumber:
        print("The number is bigger than your number")
        
    elif guess > randomNumber:
        print("The number is smaller than your number")
        
    elif guess == randomNumber:
        print(f"Congratulations! You guessed the number in {attempts} attempt(s).!")
        playAgain()
        
    if attempts == maxAttempts:
        print("Sorry! You did not manage to guess the number. You have reached the guessing limit.")
        print(f"The number was: {randomNumber}")
        playAgain()
    if not continueGame:
        print("Thank you for playing! Goodbye!")
        break






