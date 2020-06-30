# DayOfTheWeek.py
# Description: Homework 6 - This program will determine the day of the week for a given date.
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 09/23/19
# Date Last Modified: 09/26/19

def main():

    # prompt the user to input a month, day, and year
    year = int(input("Please enter the year (an integer): "))
    month = input("Please enter the month (a string): ")
    day = int(input("Please enter the day (an integer): "))

    # initialize two counters, one for months and one for days of the week
    counter1 = 1
    counter2 = 0

    # assign a specific value to "a" for the inputted month
    for i in ["March","April","May","June","July","August","September","October","Novemeber","December","January","February"]:
        if (month == i):
            a = counter1
            counter1 += 1
        else:
            counter1 += 1

    # the value of "b" is the day
    b = day
    
    # if the month is Jan. or Feb., subtract 1 from the year
    if ((month == "January") or (month == "February")):
        year -= 1

    # assign values to "c" and "d" based on the century that the inputted year is in
    if ((year>=1900) and (year<2000)):
        c = year-1900
        d = 19
    elif ((year>=2000) and (year<2100)):
        c = year-2000
        d = 20
    else:
        c = 0
        d = 21

    # Zeller's Congruence
    w = (13*a-1)//5
    x = c//4
    y = d//4
    z = w+x+y+b+c-2*d
    r = z%7
    r = (r+7)%7
    
    # determine the day of the week based on the value of "r"
    for j in ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]:
        if (r == counter2):

            # display the day of the week
            print("The day of the week is "+j+".")
            counter2 += 1
        else:
            counter2 += 1        
   
main()







    
