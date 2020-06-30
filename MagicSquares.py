# File: MagicSquares.py
# Description: HW #13: Magic Squares
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 11/15/19
# Date Last Modified: 11/15/19

class MagicSquare:

    def __init__(self,side):

        # side length and matrix (magic square)
        self.sideLength = side
        self.grid = []

        # populate matrix with zeros
        for rows in range(self.sideLength):
            self.grid.append([])
            for columns in range(self.sideLength):
                self.grid[rows].append(0)

        # starting conditions
        row = 0 
        col = self.sideLength//2
        i = 1

        # populate matrix with values
        while (i <= self.sideLength**2):
            self.grid[row][col] = i
            if (i%self.sideLength == 0):
                row += 1
            else:
                if (col == self.sideLength-1):
                    col = 0
                else:
                    col += 1
                if (row == 0):
                    row = self.sideLength-1
                else:
                    row -= 1
            i += 1

    # method for printing magic square
    def display(self):

        # print magic square
        for r in self.grid:
            for element in r:
                print(format(element,"5d"),end = "")
            print()
        print()

def main():

    # print magic squares of sizes 1,3,5,7,9,11,13
    for s in range(1,15,2):
        print("Magic Square of size",s,"\n")
        matrix = MagicSquare(s)
        matrix.display()

main()

    

    
