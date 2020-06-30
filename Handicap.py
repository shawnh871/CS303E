# File: Handicap.py
# Description: Homework 3 - This program will calculate the average and handicap for a bowler given the scores of three games.
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 09/09/2019
# Date Last Modified: 09/13/2019

def main():

    # prompt the user to input three scores
    game1 = int(input("Enter Game 1: "))
    game2 = int(input("Enter Game 2: "))
    game3 = int(input("Enter Game 3: "))

    # calculate the average score
    average = int((game1 + game2 + game3)/3)

    # calculate the handicap
    handicap = int((200 - average)*0.8)

    # display the average and handicap
    print()
    print("The bowler's average is:",average)
    print("The bowler's handicap is:",handicap)

main()

    
