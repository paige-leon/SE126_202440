#Paige Leon
#Lab #02
#Date 7/24/24
#PROGRAM PROMPT:


#Variable Dictionary
#-----------------------------------
#machine        Desktop if D, Laptop if L
#brand          DL = Dell, GW = Gateway, HP is it
#cpu            string
#ram            string
#diskOne        string
#diskTwo        string
#diskNum        int
#os             string
#year           string

#---Imports---------------
import csv

#---Main Code-------------


with open("labs_and_assignments/lab2b.csv") as file:
    file = csv.reader(file)

    #Header
    print(f"{'Type':8} | {'Brand':8} | {'CPU':4} | {'RAM':4} | {'Disk 1':8} | {'Disk 2':8} | {'No. HDD':7} | {'OS':4} | {'Year':4}")
    print("===============================================================================")

    for rec in file:
        
        #Format Machine Type
        if rec[0] == "D":
            machine = "Desktop"
        elif rec[0] == "L":
            machine = "Laptop"
        else:
            machine = "Unknown"

        #Format Brand
        if rec[1] == "DL":
            brand = "Dell"
        elif rec[1] == "HP":
            brand = "HP"
        elif rec[1] == "GW":
            brand = "Gateway"
        else:
            brand = "Unknown"
        
        #Some easy assignments
        cpu = rec[2]
        ram = rec[3]
        diskOne = rec[4]
        diskNum = int(rec[5]) #Cast as int to prep for next step

        #Check number of HDDs
        if diskNum == 1: #Only 1 disk
            diskTwo = "---"
            os = rec[6]
            year = rec[7]
        
        else: #2 disks
            diskTwo = rec[6]
            os = rec[7]
            year = rec[8]

        #output
        print(f"{machine:8} | {brand:8} | {cpu:4} | {ram:4} | {diskOne:8} | {diskTwo:8} | {diskNum:7} | {os:4} | {year:4}")

#goodbye message
print("\n\n\tThank you, goodbye :3")