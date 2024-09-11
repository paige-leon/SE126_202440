#Paige Leon
#Final!!
#9/18/24 <-- 
#PROGRAM PROMPT:


#Variable Dictionary
#-----------------------------------

#---Imports---------------
import random

#---Functions-------------
def newGame(health):
    '''Starts a new game'''

    #Set HPs
    playerHealth = health
    aiHealth = health

    #Reset deck and shuffle it
    deck = decklist.copy()
    random.shuffle(deck)

def sortAiHand(hand):
    print(hand)
    while len(aiHand) > 0:
        if aiHand[0][1] == 'Daggers':
            aiHandD.append(aiHand.pop(0))
        elif aiHand[0][1] == 'Shields':
            aiHandS.append(aiHand.pop(0))
        elif aiHand[0][1] == 'Feathers':
            aiHandF.append(aiHand.pop(0))
        elif aiHand[0][1] == 'Potions':
            aiHandP.append(aiHand.pop(0))
        else:
            print(f"ERROR: There is not a suit named {aiHand[0][1]}")
            aiHand.pop(0)
            
def draw(num):
    if num <= len(deck):
        while num > 0:
            playerHand.append(deck.pop(0))
            num -= 1
    else:
        count = 0
        while len(deck) > 0:
            playerHand.append(deck.pop(0))
            count += 1
        print(f"Deck empty.  Drew {count} cards!")

def scoreTrick(lead, follow):
    '''Return true if leading player wins the trick.  Return false if leading player lost the trick'''
    if lead[1] == follow[1]: #following player played on suit
        if lead[0] >= follow[0]: #leading player had higher value
            return True 
        else: #leading player had lower value
            return False
    return True #follwing player played off suit


def daggers(lead, follow):
    print()
def shields(lead, follow):
    print()
def feathers(lead, follow):
    print()
def potions(lead, follow):
    print()
#---Main Code-------------

#variables
decklist = [] # This is the decklist, it is not shuffled or used except to populate the deck
deck = [] #This is the deck.  It's the one thats shuffled and drawn from
discard = []

playerHand = [] #Players hand
playerHealth = 0
playerField = [] #This is where the following card goes


aiHand = []
aiHandD = []
aiHandS = []
aiHandF = []
aiHandP = []
aiHealth = 0
aiField = [] #This is where the card the ai used goes



#Create the decklist
for i in range(1, 9): #make a deck full of cards 1-8
    
    decklist.append([i, 'Daggers']) #Swords deal damage
    if i >= 3 and i <= 6:
        decklist.append([i, 'Daggers']) #Add extra middling daggers because damage is most important suit
    decklist.append([i, 'Feathers']) #Feathers draw cards
    decklist.append([i, 'Shields']) #Shields Reduce Damage
    decklist.append([i, 'Potions']) #Flasks Heal Damage

#Testing area :)))
deck = decklist.copy()
random.shuffle(deck)

newGame(20)

print(len(deck))
draw(5)
print(playerHand)
print(len(deck))
draw(100)

print(scoreTrick([1,'B'], [1,'B']))

#Main Program Loop


