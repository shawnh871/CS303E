# File: Population.py
# Description: HW #15 - Population, Benford's Law
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 12/04/19
# Date Last Modified: 12/04/19

def main():

    # initialize population dictionary
    population = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}

    # open census data file in read mode
    infile = open("2009CensusData.txt", "r")

    # skip first line, start at second line
    line = infile.readline()
    line = infile.readline()

    # read the file line by line
    while line != '':
        # traverse each character in the line
        for ch in line:
            # check if the character is a number
            if ch.isdigit():
                # traverse each key in the population dictionary
                for key in population:
                    # check if the character matches the key
                    if ch == key:
                        # if so, increment the corresponding value
                        population[key] += 1
                        break
                break
        # read the next line
        line = infile.readline()

    # find the total count
    total = 0
    
    for key in population:
        total += population[key]

    # display table header
    print(format("Digit","8s")+format("Count","10s")+"%")
    print("-"*21)

    # display the leading digits, actual frequencies, and relative frequencies
    for key in population:
        print(format(key,"9s")+format(population[key],"4d")+format(100*population[key]/total,"8.1f"))
    
        
main()
