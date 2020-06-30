# File: EasterSunday.py
# Description: Homework 2 - This program will determine the month and day of Easter Sunday for a user-inputted year.
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 09/04/19
# Date Last Modified: 09/08/19

def main():

   # prompt user to enter year
   y = int(input("Enter year: "))

   # determine month and day of Easter Sunday for the entered year
   a = y%19
   b = y//100
   c = y%100
   d = b//4
   e = b%4
   g = (8*b+13)//25
   h = (19*a+b-d-g+15)%30
   j = c//4
   k = c%4
   m = (a+11*h)//319
   r = (2*e+2*j-k-h+m+32)%7

   # month of Easter Sunday
   n = (h-m+r+90)//25

   # day of Easter Sunday
   p = (h-m+r+n+19)%32 
   
   # Display month and day of Easter Sunday for the entered year
   print("In",y,"Easter Sunday is on month",n,"and day",p)

main()
