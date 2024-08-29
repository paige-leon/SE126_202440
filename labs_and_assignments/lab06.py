#Paige Leon
#Lab #06
#8/22/24
#PROGRAM PROMPT:Write a program that can be used by a small theater to sell tickets for performances. The
#theater’s auditorium has 15 rows of seats with 30 seats in each row. The program should display
#a screen that shows which seats are available and which are taken. Seats thar are available are
#represented by # and seats that are taken are represent by a *.
#There are aisles after seats H and V.


#Variable Dictionary
#-----------------------------------
#seats[][]    15*30 array for seat availabillity chart
#rowlayout    worker variable for printing the seat map

#Notes
#in seats[][] 0 = empty and 1 = full
#---Imports---------------
from os import system, name 

#---Functions-------------
def clear(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: #For some reason my commputer kept trying to use clear despite being a windows pc so I changed this but now the program is broken on mac/linux probably :(
        _ = system('cls') 
def seatMap():
    '''Displays the seat map with # as open, * as taken, and X as ERROR'''
    
    print("Row \t\t\t\t\t\t Seats")
    print("     A  B  C  D  E  F  G  H     I  J  K  L  M  N  O  P  Q  R  S  T  U  V     W  X  Y  Z  1  2  3  4")
   
    for i in range(0, len(seats)):
        
        #Row labeling
        if i + 1 < 10: ##aligning with the help of the {var:3} format because I don't think it works like that when creating a variable to hold your string?
            rowlayout = " " + str(i + 1) + "  "
        else:
            rowlayout = str(i + 1) + "  "

        #Seats 
        for ii in range(0,len(seats[i])):
            
            #Empty
            if seats[i][ii] == 0:
                rowlayout += " # " 
            
            #Taken
            elif seats[i][ii] == 1:
                rowlayout += " * "
            
            #ERROR
            else:
                rowlayout += " X "
            
            #Aisles
            if ii == 7 or ii == 21:
                rowlayout += "   "
        
        #Print row and on to the next one
        print(rowlayout)
def menu():
    
    #clear screen and display the menu
    clear()
    seatMap()

    print("\n\n")
    print("+-----------------------+")
    print("|         ~Menu~        |")
    print("+-----------------------+")
    print("| 1. Purchase Seat(s)   |")
    print("| 2. Total Ticket Sales |")
    print("| 3. Sales Information  |")
    print("| 4. Checkout           |")
    print("| 5. Quit               |")
    print("+-----------------------+")

    entry = int(input("Please select an option: "))
    match entry:
        case 1: #Purchase Seats
            purchaseSeats()
            
        case 2: #Total Ticket Sales
            print(f"\nTicket Sales: ${totSales:0.2f}")
            input("Press [ENTER] to continue..")
            menu()

        case 3: #Sales Information
            menu()

        case 4: #Checkout
            menu()

        case 5: #Quit
            return False
        
        case _: #Invalid Entry
            input("Invalid Entry, please enter a number 1-5 (Press [ENTER] to continue)")
            menu()
def purchaseSeats():

    #Clear screen, display seating, show seat prices
    clear()
    seatMap()

    #Display Pricing menu
    print("\n\n\t\tPricing:")
    print("\t\t--------")
    print(f"\tRows  1-5 : ${priceHigh:0.2f}")
    print(f"\tRows  6-10: ${priceMid:0.2f}")
    print(f"\tRows 10-15: ${priceLow:0.2f}")

    #User input
    
    #menu()


    
  

#---Main Code-------------
seats = [[0] * 30] * 15 #Create a list that is 15 instances of 30 [0]s (a 15*30 list of 0s)
userSales = 0
userSeats = 0
totSales = 0
totSeats = 0

#Ticket Prices.  These don't change but could to quickly update prices throughout the program
priceHigh = 200
priceMid = 175
priceLow = 150

#Call Menu
menu()

#End Program
print("Good bye :3")