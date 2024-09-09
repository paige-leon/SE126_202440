#Paige Leon
#Final!!
#9/18/24 <-- 
#PROGRAM PROMPT:


#Variable Dictionary
#-----------------------------------

#---Imports---------------
import random

#---Functions-------------
def newGame():
    deck = decklist.copy()
    random.shuffle(deck)

def draw(num):
    if num <= len(deck):
        while num > 0:
            playerHand.append(deck.pop(0))
            num -= 1
    else:
        while len(deck) > 0:
            playerHand.append(deck.pop(0))

#---Main Code-------------

#variables
decklist = []
deck = []
playerHand = []
aiHand = []
discard = []

#Create the decklist
for i in range(1, 9): #make a deck full of cards 1-8
    
    decklist.append([i, 'Swords']) #Swords deal damage
    decklist.append([i, 'Feathers']) #Feathers draw cards
    decklist.append([i, 'Shields']) #Shields Reduce Damage
    decklist.append([i, 'Something Else idk what yet']) #Uh oh, idk what this'll do

#Testing area :)))
deck = decklist.copy()
random.shuffle(deck)

newGame()

print(len(deck))
draw(5)
print(playerHand)
print(len(deck))


#Main Program Loop


