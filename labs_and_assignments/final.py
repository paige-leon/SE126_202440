#Paige Leon
#Final!!
#9/18/24 <-- 
#PROGRAM PROMPT:


#Variable Dictionary
#-----------------------------------


#+-------+
#|___5___|
#|  ) (  |
#| (   ) |
#|  (_)  |
#+-------+
#+-------+
#|___5___|
#|  ___  |
#| | + | |
#|  \_/  |
#+-------+
#+-------+
#|___5___|
#|    /  |
#|  \/   |
#|  /\   |
#+-------+
#+-------+
#|___5___|
#|  / \  |
#| (=*=) |
#|  \ /  |
#+-------+
#---Imports---------------
import random

#---Functions-------------
def newGame(health,cards):
    '''Starts a new game'''

    #Set HPs
    playerHealth = health
    aiHealth = health

    #Reset deck and shuffle it
    deck = decklist.copy()
    random.shuffle(deck)

    #Draw Cards
    draw(cards, playerHand)
    draw(cards, aiHand)

def displayHand(hand):
    for i in range(0,len(hand)):
        print(f"{i}. {hand[i][0]} of {hand[i][1]}")

def sortAiHand(hand):
    '''Sort the AI hand into seperate lists sorted by suit.  This is to help the CPU player follow suit when the player is leading/to pick the leading suit when CPU is leading'''
    #print(hand)
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
            
def draw(num, hand):
    if num <= len(deck):
        while num > 0:
            hand.append(deck.pop(0))
            num -= 1
    else:
        count = 0
        while len(deck) > 0:
            hand.append(deck.pop(0))
            count += 1
        print(f"Deck empty.  Drew {count} cards!")
    if hand == aiHand:
        sortAiHand(aiHand)

def leadTrick(leader):

    if leader == True:
        displayHand(playerHand)
        try:
            choice = int(input("What card # would you like to play? "))

            playerNum = playerHand[choice][0]
            playerSuit = playerHand[choice][1]
            playerHand.pop(choice)

            print("Testing new method of field", playerNum, playerSuit)
            followTrick(choice)
        except:
            input("\n\nERROR IN leadTrick(): Please enter a valid number from the list [press ENTER to continue] ")
            leadTrick()
    else:
        suit = random.randint(1,4) #Pick a random suit and a random card from it.

        if suit == 1: #Daggers
            ran = random.randint(0,len(aiHandD)-1)
            aiNum = aiHandD[ran][0]
            aiSuit = aiHandD[ran][1]
            aiHandD.pop(ran)

        elif suit == 2: #Shields
            ran = random.randint(0,len(aiHandS)-1)
            aiNum = aiHandS[ran][0]
            aiSuit = aiHandS[ran][1]
            aiHandS.pop(ran)

        elif suit == 3: #Feathers
            ran = random.randint(0,len(aiHandF)-1)
            aiNum = aiHandF[ran][0]
            aiSuit = aiHandF[ran][1]
            aiHandF.pop(ran)
        elif suit == 4: #Potions
            ran = random.randint(0,len(aiHandP)-1)
            aiNum = aiHandP[ran][0]
            aiSuit = aiHandP[ran][1]
            aiHandP.pop(ran)

        print("ai field:",aiNum, aiSuit)
        followTrick([aiNum, aiSuit], leader) #begin the trick with the card picked by the randomizer

def followTrick(lead, leader):
    print("followTrick(lead) = ", lead)
    if leader == True:
        print("INSERT CPU AI HERE LOL")
    else:
        displayHand(playerHand)
        print(f"\nCPU has played the {lead[0]} of {lead[1]}")
        try:
            choice = int(input("What card # would you like to play? "))

            playerNum = playerHand[choice][0]
            playerSuit = playerHand[choice][1]
            playerHand.pop(choice)

            print("player", playerNum, playerSuit)
            print("ai", aiNum, aiSuit)
        except:
            input("\n\nERROR IN followTrick: Please enter a valid number from the list [press ENTER to continue] ")
            followTrick(lead)
        scoreTrick(lead, [playerNum,playerSuit], leader)


def scoreTrick(lead, follow, leader):
    '''Return true if leading player wins the trick.  Return false if leading player lost the trick'''
    if lead[1] == follow[1]: #following player played on suit
        if lead[0] >= follow[0]: #leading player had higher value
            if leader == True:
                print("You won the trick!")
            else:
                print("You lost the trick! [lower number]")
            return True 
        else: #leading player had lower value
            if leader == True:
                print("You lost the trick.. [lower number]")
            else:
                print("You won the trick!")
            leader = -playerLeading #Set the leading player into the inverse of it's current state (AKA, the leading player won the trick so they are the new leading player)
            return False
    print("You lost the trick [played off suit]")
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
playerNum = -1 #This is where the following card goes
playerSuit = ""
playerLeading = False

aiHand = []
aiHandD = []
aiHandS = []
aiHandF = []
aiHandP = []
aiHealth = 0
aiNum = -1 #This is where the card the ai used goes
aiSuit = ""



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

newGame(20,10)

print(len(deck))
draw(10,playerHand)


leadTrick(playerLeading)
#displayHand(playerHand)

#Main Program Loop



