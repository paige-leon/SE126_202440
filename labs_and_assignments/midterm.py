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
    '''clears the screen'''
    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
def cleanup():
   '''Looks over the top of the deck and removes all the [i][0] that equal 0'''
   while deck[0][IN_REGION] == 0:
        deck.pop(0)

def draw(num):
    '''Copy [num] cards from deck to hand starting at 0 and then set their IN_REGION value to False'''
    cleanup() #cleanup so all cards in list are guarenteed to be in the deck

    counter = 0

    while num > counter:
        hand.append(deck[counter].copy()) #this is crazy, who decided it was a good idea to make lists act this way
        deck[counter][IN_REGION] = False
        counter += 1
def shuffle():
    '''cleanup the deck and then shuffle'''
    cleanup()
    random.shuffle(deck)
def viewHand():
    print("UNDER CONSTRUCTION")
def stats():
    print("UNDER CONSTRUCTION")
def topdeck():
    print("UNDER CONSTRUCTION")
def discard():
    print("UNDER CONSTRUCTION")
def mill():
    print("UNDER CONSTRUCTION")
def upkeep():
    print("UNDER CONSTRUCTION")
def menu():

    cleanup()

    print("\t+-----------+")
    print(f"\t|Deck: {len(deck):2.0f}   |")
    print(f"\t|Hand: {len(hand):2.0f}   |")
    print(f"\t|Dscd: {len(discard):2.0f}   |")
    print("\t+-----------+")

    print("\n+--------------------------------+")
    print("| 1) Draw a card                 |")
    print("| 2) View Hand                   |")
    print("| 3) Check Deck Stats            |")
    print("| 4) Return Card to Top of Deck  |")
    print("| 5) Shuffle Deck                |")
    print("| 6) Discard a card              |")
    print("| 7) Mill Cards                  |")
    print("| 8) Restart                     |")
    print("| 0) Exit                        |")
    print("+--------------------------------+")

    choice = input("\n\nWhat would you like to do? ").lower()
    
    if choice == "1" or choice == "draw":
        draw(1)
        return True
    elif choice == "2" or choice == "view" or choice == "hand":
        return True
    elif choice == "3" or choice == "check":
        return True
    elif choice == "4" or choice == "return":
        return True
    elif choice == "5" or choice == "shuffle":
        shuffle()
        return True
    elif choice == "6" or choice == "discard":
        return True
    elif choice == "7" or choice == "mill":
        return True
    elif choice == "8" or choice == "restart":
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
discard = []

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
shuffle()
draw(7)

#Program Loop
cont = True
while cont == True:

    #TESTING AREA PT 2
    cont = menu()

#--------------------------Testing area
#print(deck)
shuffle()
draw(5)
for i in range(0,len(deck)):
    print(deck[i][IN_REGION])
shuffle()
for i in range(0,len(deck)):
    print(deck[i][IN_REGION])

print(hand)
test = [1,2,3,4,5]
test2 = [6,7,8,9]
test2.append(test.pop(0))
print(test)
print(test2)


