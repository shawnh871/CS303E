# File: GuessingGame.py
# Description: Homework 7 - This program will select a secret number, and the user will try to guess the number within 10 tries.
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 09/30/19
# Date Last Modified: 10/02/19

def main():

    # set secret number to 1458
    secretNumber = 1458
    # set counter to 0
    counter = 0
    # print initial prompt
    print('Welcome to the guessing game. You have ten tries to guess my number.')

    # loop for the user's 10 possible tries
    while (counter < 10):

        # prompt the user to enter a guess
        guess = int(input('Please enter your guess: '))

        # check if the guess is between 0001 and 9999
        # if not, have the user enter another guess
        while ((guess < 0) or (guess >= 10000)):
            print('Your guess must be between 0001 and 9999.')
            guess = int(input('Please enter a valid guess: '))

        # if it is, increment the counter for the number of guesses
        counter += 1

        # guess is too low
        if (guess < secretNumber):
            print('Your guess is too low.\nGuesses so far:',counter)

        # guess is too high
        elif (guess > secretNumber):
            print('Your guess is too high.\nGuesses so far:',counter)

        # guess is correct
        else:
            
            # correct on the first try
            if (counter == 1):
                print('That\'s correct!\nCongratulations! You guessed it on the first try!')
                break

            # correct guess within the first 10 tries, excluding the first try
            else:
                print('That\'s correct!\nCongratulations! You guessed it in',counter,'guesses.')
                break
            
    # if it is the user's 10th guess and the guess is not correct, it's game over
    if (guess != secretNumber):
        print('Game over: you ran out of guesses.')
            
main()



        

    
    
