# File: Report.py
# Description: Homework 8 - This program will print a data report in a specific format.
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 10/10/19
# Date Last Modified: 10/10/19

def main():

    # input data
    companyName = "Lone Star Corporation"
    date = "October 1, 2019"
    cash = 7505.54
    acctsRec = 502.21
    supplies = 313.89
    land = 6456.23
    buildings = 81598.00
    machAndEquip = 8329.99
    patents = 2000.00
    acctsPay = 93569.23
    stock = 88100.00

    # calculate total assets and liabilities
    totalAssets = cash + acctsRec + supplies + land + buildings + machAndEquip + patents
    totalLibAndStock = acctsPay + stock

    # print report header
    print()
    print(companyName.upper().center(80))
    print("Balance Sheet".center(80))
    print(date.center(80))
    print()

    # print table header
    print(format(" ","42s"),format("Liabilities and","37s"))
    print(format("Assets","45s"),format("Stockholders' Equity","34s"))

    # print line
    for i in range(80):
        print("-",end="")
    print()

    # print data
    print(format(" ","2s"),format("Cash","28s"),format(cash,"8.2f")," ",format("Liabilities","38"))
    print(format(" ","2s"),format("Accounts Receivable","28s"),format(acctsRec,"8.2f"),format(" ","4s"),format("Accounts Payable","25s"),format(acctsPay,"8.2f"))
    print(format(" ","2s"),format("Supplies","28s"),format(supplies,"8.2f"))
    print(format(" ","2s"),format("Land","28s"),format(land,"8.2f"))
    print(format(" ","2s"),format("Buildings","28s"),format(buildings,"8.2f"),format(" ","4s"),"Stockholders' Equity:")
    print(format(" ","2s"),format("Machines and Equipment","28s"),format(machAndEquip,"8.2f"),format(" ","6s"),format(" Capital Stock","23s"),format(stock,"8.2f"))
    print(format(" ","2s"),format("Patents","28s"),format(patents,"8.2f"))
    print()
    print(format("Total Assets","30s"),format(totalAssets,"9.2f"),"  Total Liabilities and")
    print(format(" ","45s"),format("Stockholders' Equity","24s"),format(totalLibAndStock,"9.2f"))
    print()

main()
