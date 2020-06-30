# File: Combinations.py
# Description: Homework 9 - This program will print a table that lists the number of possible hands with a certain number of cards.
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 10/11/19
# Date Last Modified: 10/14/19

# factorial function
def factorial(num):

    # initialize factorial variable
    numFact = 1

    # calculate factorial
    for i in range(1,num+1):
        numFact = numFact * i

    return numFact

# combinations function
def combinations(n,r):

    # calculate number of combinations
    comb = factorial(n)/(factorial(r)*(factorial(n-r)))

    return comb

def main():

    # print table header
    print()
    print(format("Cards","9s"),"Combinations")

    # print line
    for j in range(22):
        print("=",end="")

    print()

    # print table values
    for number in range(53):
        print(format(number,"3.0f"),format(combinations(52,number),"18.0f"))
    print()            

main()
        
