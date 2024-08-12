#Paige Leon
#Lab 04
#Date 8/7/24
#PROGRAM PROMPT:


#Variable Dictionary
#-----------------------------------
#nameFirst = []     \
#nameLast = []       \
#age = []             \
#nickname = []        /------Parallel lists.  All Strings except age 
#house = []          /
#motto = []         /
#count = 0           Total number of people scanned
#totAge = 0          Total age of all people combined.  Used for calculating avg
#avgAge              totAge/count
#starks = ""         \
#baratheons = ""      \
#tullys = ""            -----  [variable name] += "|" to tally house counts
#watchs = ""          /
#lannisters = ""     /
#targaryens = ""    /

#---Imports---------------
import csv

#---Main Code-------------

#initialize parallel lists
nameFirst = []
nameLast = []
age = []
nickname = []
house = []
motto = []

#worker variables
count = 0
totAge = 0
starks = ""
baratheons = ""
tullys = ""
watchs = ""
lannisters = ""
targaryens = ""

#connected to file----------------------------------------------
with open("labs_and_assignments/lab4A_GOT_NEW.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        nameFirst.append(rec[0])
        nameLast.append(rec[1])
        age.append(float(rec[2]))
        nickname.append(rec[3])
        house.append(rec[4])
        
#disconnect----------------------------------------------------

#Print the top list 
print(f"{"First Name":10}\t| {"Last Name":10}\t| {"Age":3}\t| {"Nickname":15}\t| {"House":15}")
print("===============================================================================")

#Print the list 
for i in range(0, len(nameFirst)):
    
    #increase count for later
    count += 1
    totAge += age[i]

    #print parallel list stuff
    print(f"{nameFirst[i]:10}\t| {nameLast[i]:10}\t| {age[i]:3.0f}\t| {nickname[i]:15}\t| {house[i]:15}")

#============Print list with mottos!=============

#Print the top list 
print(f"\n\n{"First Name":10}\t| {"Last Name":10}\t| {"Age":3}\t| {"Nickname":15}\t| {"House":15}\t| {"Motto":10}")
print("================================================================================================================")
for i in range(0, len(house)):
    
    #assign a motto based on house name.  Shrimple as that
    if house[i] == "House Stark":
        starks += "|"
        motto.append("It's so so cold :(")
    elif house[i] == "House Baratheon":
        baratheons += "|"
        motto.append("We're gumpy >:(")
    elif house[i] == "House Tully":
        tullys += "|"
        motto.append("Live. Laugh. Love")
    elif house[i] == "Night's Watch":
        watchs += "|"
        motto.append("Five Nights at Freddy's")
    elif house[i] == "House Lannister":
        lannisters += "|"
        motto.append("rawr >:3")
    elif house[i] == "House Targaryen":
        targaryens += "|"
        motto.append("Dragon Tales")

    #print parallel list stuff
    print(f"{nameFirst[i]:10}\t| {nameLast[i]:10}\t| {age[i]:3.0f}\t| {nickname[i]:15}\t| {house[i]:15}\t| {motto[i]:20}")

#----------------Avg age and tallies----------------------
avgAge = totAge / count
print(f"\n\n\t\t Total People: {count}")
print(f"\t\t  Average Age: {avgAge:.0f}")
print("\t\t=========================")
print(f"\t\t       Starks:{starks}")
print(f"\t\t   Baratheons:{baratheons}")
print(f"\t\t       Tullys:{tullys}")
print(f"\t\tNights Watchs:{watchs}")
print(f"\t\t   Lannisters:{lannisters}")
print(f"\t\t   Targaryens:{targaryens}")

print("\n\nGoodbye :3")