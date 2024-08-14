#Paige Leon
#Midterm
#Date 8/19/24
#PROGRAM PROMPT:


#Variable Dictionary
#-----------------------------------

#---Imports---------------
import random
import csv

#---Functions-------------


#---Main Code-------------

#variables
indeck = []
cname = []
cvalue = []
deck = []

#open document
with open("labs_and_assignments/cards.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        indeck.append(1)
        cname.append(rec[0])
        cvalue.append(rec[1])
        
#Close document



print(deck)
test = [1,2,3,4,5,6,7,8,9]

print(test)
random.shuffle(test)
print(test)