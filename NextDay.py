# File: NextDay.py
# Description: Homework 5 - This program will determine the next day given the inputted day.
# Student's Name: Shao-Po Huang
# Stident's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 09/20/19
# Date Last Modified: 09/23/19

def main():

    # prompt the user to input month, day, and year
    year = int(input("Please enter the year: "))
    month = input("Please enter the month: ")
    day = int(input("Please enter the day: "))
    
    # check if the month entered has 31 days (Jan, Mar, May, Jul, Aug, Oct, Dec)
    if ((month == "January") or (month == "March") or (month == "May") or (month == "July") or (month == "August") or (month == "October") or (month == "December")):

        # if the day entered is not the last day of the month, increment the day
        if (day != 31):
            day += 1

        # otherwise (it is the last day of the month), reset the day to 1 and change the month to the following month
        else:
            day = 1
            if (month == "January"):
                month = "February"
            elif (month == "March"):
                month = "April"
            elif (month == "May"):
                month = "June"
            elif (month == "July"):
                month = "August"
            elif (month == "August"):
                month = "September"
            elif (month == "October"):
                month = "November"

            # if the month is December, increment the year as well
            else:
                month = "January"
                year += 1
    
    # check if the month entered has 30 days (Apr, Jun, Sep, Nov)
    elif ((month == "April") or (month == "June") or (month == "September") or (month == "November")):

        # if the day entered is not the last day of the month, increment the day
        if (day != 30):
            day += 1

        # otherwise (it is the last day of the month), reset the day to 1 and change the month to the following month
        else:
            day = 1
            if (month == "April"):
                month = "May"
            elif (month == "June"):
                month = "July"
            elif (month == "September"):
                month = "October"
            else:
                month = "December"

    # the month is February
    else:

        # check if it is the 28th of February
        if (day == 28):
            
            # if it is a leap year, increment the day
            if ((year%4 == 0 and year%100 != 0) or (year%400 == 0)):
                day += 1

            # otherwise (non-leap year), reset the day to 1 and change the month to March
            else:
                month = "March"
                day = 1

        # if it is the 29th of February (leap year), reset the day to 1 and change the month to March
        elif (day == 29):
            month = "March"
            day = 1

        # otherwise (not the last day of the month), increment the day
        else:
            day += 1

    # display the month, day, and year of the next day
    print("The next day is "+month+" "+str(day)+", "+str(year)+".")

main()

        
