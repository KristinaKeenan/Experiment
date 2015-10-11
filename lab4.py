#Kristina Keenan

#2/19/15

#The purpose of this program is to have a user try to guess a number between 1 and 10 in three tries.


#This program has the computer come up with a random number between 1 and 10, then have a user try to guess it by inputting data up to times. After each guess, the program
#lets the user know if they are higher, lower, or equal to the random number and allows them to try again, unless they have used all of their guesses, then it either displays
#a winning message or a failure message with the answer, asking the player if they want to play again.

import random

def guessing(number):

    """This function allows the user to guess the secret number and tells him or her if she is high, lower, or equal to the number."""

    numTries = 0

    right = False

    #tells you if the guess is higher, lower, or equal to the secret number
    while numTries < 3:
        guess = int(input("What is your guess?"))
        if guess > number:
            print("Your guess was too high.")
            numTries = numTries + 1
            right = False
            
        elif guess < number: 
            print("Your guess is too low.")
            numTries = numTries + 1
            right = False

        else: 
            print("You guessed it!")
            numTries = 3
            right = True


    #asks the user if they want to try again, and either calls the main function or ends the program
    while numTries == 3:
        
        if right:
            
            tryAgain = input("Try again?")
            if tryAgain == "yes":
                main()
            else:
                print("Goodbye.")
                right = False

            return tryAgain
            
            
        else:
            
            print("The answer was", number)
            tryAgain = input("Try again?")
            if tryAgain == "yes":
                main()
            else:
                print("Goodbye.")

            return tryAgain

    
    
        
      
            

def main():
    """This function is the main function, which tells the user what to input and then creates the secret number. It then calls the guessing function."""

    #starts game, thinks of secret number, calls guessing function
    print("I'm thinking of a number between 1 and 10, can you get it in 3 tries?")
    secretNumber = random.randrange(1, 10)
    guessing(secretNumber)
    
                
main()
