# File: Grades.py
# Description: HW #14: Grade Book
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 11/22/19
# Date Last Modified: 11/22/19

def main():

    # open input file
    infile = open("gradeInput.txt", "r")

    # open output file
    outfile = open("gradeOutput.txt", "a")

    # write table header into output file
    outfile.write(" "*33+format("HW","7s")+format("Exam","7s")+"Final\n")
    outfile.write(format("Last Name","15s")+format("First Name","18s")+format("Avg","7s")*2+"Grade\n")
    outfile.write("-"*52+"\n")

    # process input file data
    for line in infile:

        # initialize HW grade sum, exam grade sum, last name string, and first name string
        hwSum = examSum = 0
        lastName = firstName = ""

        # set boolean for finding comma in the name
        foundComma = False

        # isolate the first and last names
        myList = line.split()
        for ch in myList[0]:
            if (ch.isalpha() and (not foundComma)):
                lastName += ch
            else:
                foundComma = True
                if(ch.isalpha()):
                    firstName += ch

        # calculate the homework average
        for i in range(1,16):
            hwSum += eval(myList[i])
        hwAvg = hwSum/15

        # calculate the exam average
        for j in range(16,19):
            examSum += eval(myList[j])
        examAvg = examSum/3

        # calculate the final grade
        finalGrade = 0.55 * hwAvg+ 0.45 * examAvg

        # write students' first and last names, homework averages, exam averages, and final grades into output file
        outfile.write(format(lastName,"15s")+format(firstName,"15s")+format(hwAvg,"7.1f")+format(examAvg,"7.1f")+format(finalGrade,"7.1f")+" \n")

main()
