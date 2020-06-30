# File: Deal.py
# Description: Homework 10 - Let's Make a Deal - Savant strategy simulation
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 10/22/19
# Date Last Modified: 10/23/19

# import random package
import random

# random number generator
def roll(n):
    
    return random.randint(1,n)

# run one trial of the game in which the user switches his/her guess
def runOneTrial():

    # generate and display prize door number
    prize = roll(3)
    print(format(prize,">6d"),end="")

    # generate and display guess door number
    guess = roll(3)
    print(format(guess,">7d"),end="")

    # generate and display view door number
    view = 1
    while (view == guess or view == prize):
        view += 1

    print(format(view,">7d"),end="")

    # generate and display new guess (switch) door number
    newGuess = 1    
    while (newGuess == guess or newGuess == view):
        newGuess += 1

    print(format(newGuess,">9d"))

    # check if the user won or lost
    if (newGuess == prize):
        return "win"

    else:
        return "lose"

def main():

    # prompt the user to input number of trials
    trials = int(input("\n   How many trials do you want to run? "))

    # initialize win counter 
    wins = 0

    # display table header
    print("\n   Prize  Guess  View  New Guess")  

    # run user-specified number of trials while keeping track of the number of wins
    for i in range(trials):
    
        if (runOneTrial() == "win"):
            wins += 1

    # calculate probability of winning by switching
    switchWin = wins/trials

    # calculate probability of winning by not switching
    stayWin = 1 - switchWin

    # display both probabilities
    print("\n   Probability of winning if you switch =", format(switchWin,"3.1f"))
    print("   Probability of winning if you do not switch =", format(stayWin,"3.1f"),end="\n\n")
    
main()
   
