#Paige Leon
#Lab Week 4
#Date 8/724
#PROGRAM PROMPT: Process file, print.  Find average in # and letter.  Print again.


#Variable Dictionary
#-----------------------------------
#firstNames = []  \
#lastNames = []    \
#test1 = []          >---Parallel list of stuff from the document.  tests are stored as ints
#test2 = []        /
#test3 = []       /


#avgNum = []  \
#               >------Parallel with each other and above lists.  Avg in numeric and avg as letter grade
#avgLet = []  /

#---Imports---------------
import csv


#---Main Code-------------
#Create empty lists
firstNames = []
lastNames = []
test1 = []
test2 = []
test3 = []


avgNum = []
avgLet = []

#connected to file----------------------------------------------
with open("labs_and_assignments/listPractice1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        firstNames.append(rec[0])
        lastNames.append(rec[1])

        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnect-----------------------------------------------------

#Part 1 (print the list)
print(f"\n\n{"First Name":10}\t|{"Last Name":10}\t|{"Gr1":3}\t|{"Gr2":3}\t|{"Gr3":3}")
print("====================================================")
for i in range(0, len(firstNames)):
    print(f"{firstNames[i]:10}\t|{lastNames[i]:10}\t|{test1[i]:3}\t|{test2[i]:3}\t|{test3[i]:3}")

#Part 2 (Reprocess to figure out grade avg/letters)
for i in range( 0, len(firstNames)):
    avg = (test1[i] + test2[i] + test3[i]) / 3
    avgNum.append(avg)

    if avg >= 90:
        avgLet.append("A")
    elif avg >= 80:
        avgLet.append("B")
    elif avg >= 70:
        avgLet.append("C")
    elif avg >= 60:
        avgLet.append("D")
    else:
        avgLet.append("F")


#table of contents
print(f"\n\n{"First Name":10}\t|{"Last Name":10}\t|{"Gr1":3}\t|{"Gr2":3}\t|{"Gr3":3}\t{"Avg":3}\t|{"Let":3}")
print("===================================================================")

#print data
for i in range(0, len(firstNames)):
    print(f"{firstNames[i]:10}\t|{lastNames[i]:10}\t|{test1[i]:3}\t|{test2[i]:3}\t|{test3[i]:3}\t|{avgNum[i]:3.0f}\t|{avgLet[i]:3}")

#Goodbye
print("\n\n\t Good bye :3")