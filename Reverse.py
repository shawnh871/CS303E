# File: Reverse.py
# Description: Homework 4 - This program will reverse a four-digit number.
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 09/13/19
# Date Last Modified: 09/17/19

def main():

    # prompt user to enter an integer
    yourNumber = int(input("Enter an integer: "))

    # determine ones digit by finding the remainder after dividing the four-digit number by 10
    onesDigit = yourNumber%10

    # determine tens digit
    # subtract the ones digit from the four-digit number
    secondNumber = yourNumber - onesDigit
    # divide by 10 to get a three-digit number, then repeat the remainder step to get the tens digit
    tensDigit = (secondNumber//10)%10

    # determine hundreds digit
    # subtract the tens digit from the three-digit number
    thirdNumber = secondNumber//10 - tensDigit
    # divide by 10 to get a two-digit number, then repeat the remainder step to get the hundreds digit
    hundDigit = (thirdNumber//10)%10

    # determine thousands digit
    # subtract the hundreds digit from the two-digit number
    fourthNumber = thirdNumber//10 - hundDigit
    # divide by 10 to get the thousands digit
    thousDigit = fourthNumber//10

    # calculate the reversed number
    # take the sum of the products of the digits and the powers of 10 in reverse order
    reverse = onesDigit*1000 + tensDigit*100 + hundDigit*10 + thousDigit

    # display reversed number
    print("The reversed number is",reverse,end=".")
    

main()
