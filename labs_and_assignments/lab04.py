#Paige Leon
#Lab 04
#Date 8/7/24
#PROGRAM PROMPT:


#Variable Dictionary
#-----------------------------------

#---Imports---------------
import csv

#---Main Code-------------

#initialize parallel lists
nameFirst = []
nameLast = []
age = []
nickname = []
house = []

#connected to file----------------------------------------------
with open("labs_and_assignments/lab4A_GOT_NEW.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        nameFirst.append(rec[0])
        nameLast.append(rec[1])
        age.append(rec[2])
        nickname.append(rec[3])
        house.append(rec[4])
        
#disconnect----------------------------------------------------
