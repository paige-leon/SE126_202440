import csv

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

for i in range(0, len(firstNames)):
    print(f"{firstNames[i]:10}\t{lastNames[i]:10}\t{test1[i]:3}\t{test2[i]:3}\t{test3[i]:3}")


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