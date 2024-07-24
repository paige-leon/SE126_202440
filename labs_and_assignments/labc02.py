#Paige Leon
#Class Lab Week 2
#7/24/24
#PROGRAM PROMPT: Write a program that displays all rooms that are over maximum limit of people and the number of people that have to be notified 
#that they will have to be put on the waitlist.  After the file is processed, display number of records processed and the number of rooms over the top


#Variable Dictionary
#rec_count      counts number of times for loop runs
#over_count     counts number of times if statement triggers

#Note:
#The room file is organized as follows  [Name, Room Capacity, Attendants] 
#-----------------------------------

#---Imports---------------
import csv

#---Main Code-------------

#Counting Variables
rec_count = 0
over_count = 0

#Open up file at relative path
with open("labs_and_assignments/lab2a.csv") as file:
    file = csv.reader(file)
    
    #header + horizontal divider
    print(f"{'LOCATION':20} |\t {" MAX":6} |\t {"ATTENDANTS":10} |\t {"  OVER":6}")
    print("================================================================")

    #For loop
    for rec in file:

        #incriment counter
        rec_count += 1

        #Check if more attendants than capacity
        if int(rec[2]) > int(rec[1]): #need to cast as ints
            
            #incriment other counter
            over_count += 1

            #calculate amount over the limit
            over = int(rec[2]) - int(rec[1])

            #output
            print(f"{rec[0]:20} |\t {rec[1]:6} |\t {int(rec[2]):10} |\t {over: 6}")

#Final output
print(f"\n\n\tTotal of {rec_count} records checked.")
print(f"\tThere were {over_count} rooms over the maximum capacity")

#Goodbye message
print("\n\n\nThank you. Goodbye :3")