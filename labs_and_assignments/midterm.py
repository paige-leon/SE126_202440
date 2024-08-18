#Paige Leon
#Midterm
#Date 8/19/24
#PROGRAM PROMPT:


#Variable Dictionary
#-----------------------------------

#---Imports---------------
import random
import csv
from os import system, name 


#---Functions-------------
def clear(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: #For some reason my commputer kept trying to use clear despite being a windows pc so I changed this but now the program is broken on mac/linux probably :(
        _ = system('cls') 
def cleanup():
   '''Looks over the top of the deck and removes all the [i][0] that equal 0'''
   while deck[0][IN_REGION] == 0:
        deck.pop(0)

def draw(num):
    '''Copy [num] cards from deck to hand starting at 0 and then set their IN_REGION value to False'''
    cleanup() #cleanup so all cards in list are guarenteed to be in the deck

    counter = 0

    while num > counter:
        print(f"Drew: {deck[counter][NAME]}")
        hand.append(deck[counter].copy()) #this is crazy, who decided it was a good idea to make lists act this way
        deck[counter][IN_REGION] = False
        counter += 1
    input("\n\n Press [ENTER] to continue: ")


def shuffle():
    '''cleanup the deck and then shuffle'''
    cleanup()
    random.shuffle(deck)
def viewZone(zone):
    
    print(f"\n\n # | {"Name":30} |\t {"Card Type":12} |\t {"M.Cost":6}")
    print("================================================================")
    for i in range(0,len(zone)):
        print(f"{i:2.0f} | {zone[i][NAME]:30} |\t {zone[i][TYPE]:12} |\t {zone[i][MANACOST]:6}")

def stats():
    print("UNDER CONSTRUCTION")

def topdeck(num):
    cleanup()
    deck.insert(0,hand.pop(num))

def discard(num):
    graveyard.append(hand.pop(num))

def mill():

    #Clear screen, cleanup deck, and display cards in all zones
    clear()
    cleanup()
    zoneInfo()

    choice = input("How many cards would you like to mill? ")

    try:
        count = int(choice)
        while count > 0:
            print(f"Milled: {deck[0][NAME]}")
            graveyard.append(deck.pop(0))
            count -= 1
        print(f"\n{choice} cards milled.")
        input("\nPress [ENTER] to continue: ")

    except:
        print("\n\n\t***INVALID ENTRY***")
        print("\tInput must be a positive integer. Please try again")
        input("Press [ENTER] to continue: ")
        mill()


def upkeep():
    print("*ALERT*")
    print("Are you sure you want to restart?  You cannot undo this")
    choice = input("[YES/NO]").lower()
    if choice == "yes":
        
        #remove items from lists until 100% empty
        while len(deck) > 0:
            deck.pop(0)
        while len(hand) > 0:
            hand.pop(0)
        while len(graveyard) > 0:
            graveyard.pop(0)

        for i in range(0,len(decklist)):
            deck.append(decklist[i])
        
        #Shuffle and Draw 7
        shuffle()
        draw(7)

    else:
        input("Returning to Main Menu.  Press [ENTER] to continue: ")

def zoneInfo():
    print("\t+-----------+")
    print(f"\t|Deck: {len(deck):2.0f}   |")
    print(f"\t|Hand: {len(hand):2.0f}   |")
    print(f"\t|Dscd: {len(graveyard):2.0f}   |")
    print("\t+-----------+")

def handMenu():
    choice = -1
    
    while choice != "0":
        clear()
        zoneInfo()
        viewZone(hand)
        print("+------------------------+")
        print("| 1) Discard a card      |")
        print("| 2) Top deck a card     |")
        print("| 0) Return to Main Menu |")
        print("+------------------------+")

        choice = input("\n\n\tWhat do you want to do? ").lower()

        if choice == "1":
            choice2 = input("\tWhich card # you want to discard? ")

            try:
                choice2 = int(choice2)
                discard(choice2)

            except:
                input(f"ERROR: Input must be an integer between 0 and {len(hand) - 1}")
        elif choice == "2":
            choice2 = input("\tWhich card # you want to return to the top of the deck? ")

            try:
                choice2 = int(choice2)
                topdeck(choice2)

            except:
                input(f"ERROR: Input must be an integer between 0 and {len(hand) - 1}")
        elif choice != "0":
            clear()
            print("***ERROR: Invalid Entry***")
        

def menu():

    #cleanup deck and clear the screen
    cleanup()
    clear()

    #Display Deck,Hand,Graveyard sizes
    zoneInfo()

    print("\n+--------------------------------+")
    print("| 1) Draw a card                 |")
    print("| 2) View Hand                   |")
    print("| 3) Check Deck Stats            |")
    print("| 4) Shuffle Deck                |")
    print("| 5) Mill Cards                  |")
    print("| 6) View Deck                   |")
    print("| 7) Check Graveyard             |")
    print("| 8) View Decklist               |")
    print("| 9) Restart                     |")
    print("| 0) Exit                        |")
    print("+--------------------------------+")

    choice = input("\n\nWhat would you like to do? ").lower()
    
    if choice == "1" or choice == "draw":
        draw(1)
        return True
    elif choice == "2" or choice == "view" or choice == "hand":
        clear()
        handMenu()
        return True
    elif choice == "3" or choice == "check":
        stats()
        return True
    elif choice == "4" or choice == "shuffle":
        shuffle()
        input("Deck Shuffled: Press [ENTER] to continue: ")
        return True
    elif choice == "5" or choice == "mill":
        mill()
        return True
    elif choice == "6" or choice == "deck":
        viewZone(deck)
        input("\n\n Press [ENTER] to continue: ")
        return True
    elif choice == "9" or choice == "restart":
        upkeep()
        return True
    elif choice == "7" or choice == "graveyard":
        viewZone(graveyard)
        input("\n\n Press [ENTER] to continue: ")
        return True
    elif choice == "8" or choice == "decklist":
        viewZone(decklist)
        input("\n\n Press [ENTER] to continue: ")
        return True
    elif choice == "0" or choice == "exit":
        return False
    else:
        print("\n\n\t***Invalid Entry***")
        print(f"{choice} is not a valid command. Please try again")

    
#---Main Code-------------

#------Variables----------

#Constants for deck list handling DO NOT UNDER ANY CIRCUMSTANCES CHANGE THE VALUES OF THESE VARIABLES
IN_REGION = 0
NAME = 1
TYPE = 2
MANACOST = 3
CMC = 4


#parallel arrays, used to create the 2D list, 'deck' later
quantity = []
name = []
type = []
manaCost = []
cmc = []

#Variables that are actually used more than once
deck = []
hand = []
graveyard = []

#-----Program initialization process.  Open doc, make cards, add to deck--------
#open document
with open("labs_and_assignments/cards.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        quantity.append(int(rec[0]))
        name.append(rec[NAME])
        
        #Card Type
        if rec[TYPE].lower() == "c":
            type.append("Creature")

        elif rec[TYPE].lower() == "i":
            type.append("Instant")   

        elif rec[TYPE].lower() == "s":
            type.append("Sorcery")   

        elif rec[TYPE].lower() == "e":
            type.append("Enchantment")  

        elif rec[TYPE].lower() == "a":
            type.append("Artifact")

        elif rec[TYPE].lower() == "l":
            type.append("Land")   

        elif rec[TYPE].lower() == "p":
            type.append("Planeswalker")

        #mana cost + cmc (converted mana cost)
        manaCost.append(rec[MANACOST])
        cmc.append(rec[CMC])           
#Close document

#Assemble the deck for the first time
for i in range(0, len(quantity)):
    card = []
    card.append(True)
    card.append(name[i])
    card.append(type[i])
    card.append(manaCost[i])
    card.append(cmc[i])

    for ii in range(0, quantity[i]):
        deck.append(card.copy()) #apparently python is crazy so if you dont do this when you change a value in one list it'll change all of them???????

#Create 2nd version of deck.  This one will only be viewed, never shuffled, or altered
decklist = deck.copy()
decksize = len(decklist)

#Shuffle and then Draw 7 cards at the start because that's how Magic works
zoneInfo()
shuffle()
draw(7)

#Program Loop
cont = True
while cont == True:

    cont = menu()

#--------------------------Testing area
#print(deck)
#shuffle()
#draw(5)
#for i in range(0,len(deck)):
#    print(deck[i][IN_REGION])
#shuffle()
#or i in range(0,len(deck)):
#   print(deck[i][IN_REGION])
#print(hand)
#test = [1,2,3,4,5]
#test2 = [6,7,8,9]
#est2.append(test.pop(0))
#print(test)
#print(test2)


