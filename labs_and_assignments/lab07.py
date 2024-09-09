#Paige Leon
#Lab #7
#Date 8/28/24
#PROGRAM PROMPT:


#Variable Dictionary
#-----------------------------------

#---Imports---------------
import csv

#---Functions-------------
def menu():

    #Display Menu
    print("\n+--------------------------------+")
    print("|             ~Menu~             |")
    print("| 1. See All Student Report      |")
    print("| 2. Search for a Student [ID]   |")
    print("| 3. Search for a Student [Last] |")
    print("| 4. View a Class Roster         |")
    print("| 0. Exit Program                |")
    print("+--------------------------------+")

    return input("\n\nWhat would you like to do? [1-4 or 0]: ")


def bineySearch():
    print("Your search doesn't have a biney?")

#---Main Code-------------

#Parallel Lists
ids = []
namesLast = []
namesFirst = []
classes1 = []
classes2 = []
classes3 = []

foundClasses = []

#Open file
with open("labs_and_assignments/lab5_students.txt") as csvfile:
    file = csv.reader(csvfile)

    #Create all them lists
    for rec in file:
        ids.append(int(rec[0]))
        namesLast.append(rec[1])
        namesFirst.append(rec[2])
        classes1.append(rec[3])
        classes2.append(rec[4])
        classes3.append(rec[5])
#Close File

#Initialize looping var
choice = -1

#Main Porgram loop
while choice != "0":
    
    #Call the Menu function to make option
    choice = menu()

    #See all Student Report
    if choice == "1":
        print("\n\t\t\t\t\t  ~Class Roster~")
        print(f"{"ID":4} |\t {"Last Name":15} |\t {"First Name":15} |\t {"Class1":6}  |\t {"Class2":6} |\t {"Class3":6}")
        print("=" * 100)

        for i in range(0,len(ids)):
            print(f"{ids[i]:4} |\t {namesLast[i]:15} |\t {namesFirst[i]:15} |\t {classes1[i]:6}  |\t {classes2[i]:6} |\t {classes3[i]:6}")

    #Search ID
    elif choice == "2":
        print()

    #Search Last Name
    elif choice == "3":
        print()

    #View Class Roster (seq search c1,c2+c3)
    elif choice == "4":

        classSearch = input("What class's roster do you want to view?: ")
        
        #Check the lists for classSearch and add index to foundClass[]
        for i in range(0,len(classes1)):
        
            if classSearch == classes1[i]:
                foundClasses.append(i)
            elif classSearch == classes2[i]:
                foundClasses.append(i)
            elif classSearch == classes3[i]:
                foundClasses.append(i)

        #Print out ID, First Name, Last name
        #If foundClasses is empty (no students found)
        if not foundClasses: 
            print(f"It seems no students are enrolled in {classSearch}.")
        
        #if foundClasses isn't empty
        else:
            print(f"The following students are taking {classSearch}:")
            for i in range(0, len(foundClasses)):
                print(f"{ids[foundClasses[i]]:4} | {namesFirst[foundClasses[i]]:10} | {namesLast[foundClasses[i]]:20}")

        #Clear the foundClasses list to prepare for next time
        foundClasses.clear()

    #Exit
    elif choice == "0":
        print("Thank you for me. Goodbye :3")