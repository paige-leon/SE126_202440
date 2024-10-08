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
            choice = int(input("What card # would you like to lead with? "))

            playerNum = playerHand[choice][0]
            playerSuit = playerHand[choice][1]
            playerField = playerHand.pop(choice)

            return playerField
        except:
            input("\n\nERROR IN leadTrick(): Please enter a valid number from the list [press ENTER to continue] ")
            leadTrick()
    
    #AI Leading Trick
    
    else:
        validChoice = False
        while validChoice == False:

            try:
                suit = random.randint(1,4) #Pick a random suit and a random card from it.

                if suit == 1: #Daggers
                    ran = random.randint(0,len(aiHandD)-1)
                    aiNum = aiHandD[ran][0]
                    aiSuit = aiHandD[ran][1]
                    aiField = aiHandD.pop(ran)

                elif suit == 2: #Shields
                    ran = random.randint(0,len(aiHandS)-1)
                    aiNum = aiHandS[ran][0]
                    aiSuit = aiHandS[ran][1]
                    aiField = aiHandS.pop(ran)

                elif suit == 3: #Feathers
                    ran = random.randint(0,len(aiHandF)-1)
                    aiNum = aiHandF[ran][0]
                    aiSuit = aiHandF[ran][1]
                    aiField = aiHandF.pop(ran)
                elif suit == 4: #Potions
                    ran = random.randint(0,len(aiHandP)-1)
                    aiNum = aiHandP[ran][0]
                    aiSuit = aiHandP[ran][1]
                    aiField = aiHandP.pop(ran)
                validChoice = True
            
            except:
                print("Thinking...")
        

        return aiField        

def followTrick(lead, leader):
    if leader == True:
        
        #Find the max and min for on/off suit play win/lose
        max = 0
        maxID = -1
        min = 100
        minID = -1
        offSuit = False

        #Leading Daggars
        if lead[1] == "Daggers":

            #AI Has on suit option
            if len(aiHandD) != 0:
                for i in range(0,len(aiHandD)):
                    if aiHandD[i][0] > max:
                        max = aiHandD[i][0]
                        maxID = i
                    if aiHandD[i][0] < min:
                        min = aiHandD[i][0]
                        minID = i
                if max < lead[0]: #Return smallest on suit if can't win
                    aiField = aiHandD.pop(minID)
                else: #Return highest on suit if can win
                    aiField = aiHandD.pop(maxID)
            else:
                offSuit = True

        #Leading Shields
        elif lead[1] == "Shields":
            
            #AI Has on suit option
            if len(aiHandS) != 0:
                for i in range(0,len(aiHandS)):
                    if aiHandS[i][0] > max:
                        max = aiHandS[i][0]
                        maxID = i
                    if aiHandS[i][0] < min:
                        min = aiHandS[i][0]
                        minID = i
                if max < lead[0]: #Return smallest on suit if can't win
                    aiField = aiHandS.pop(minID)
                else: #Return highest on suit if can win
                    aiField = aiHandS.pop(maxID)
            else:
                offSuit = True

        #Leading Feathers
        elif lead[1] == "Feathers":
            
            #AI Has on suit option
            if len(aiHandF) != 0:
                for i in range(0,len(aiHandF)):
                    if aiHandF[i][0] > max:
                        max = aiHandF[i][0]
                        maxID = i
                    if aiHandF[i][0] < min:
                        min = aiHandF[i][0]
                        minID = i
                if max < lead[0]: #Return smallest on suit if can't win
                    aiField = aiHandF.pop(minID)
                else: #Return highest on suit if can win
                    aiField = aiHandF.pop(maxID)
            else:
                offSuit = True

        #Leading Potions       
        elif lead[1] == "Potions":
            #AI Has on suit option
            if len(aiHandP) != 0:
                for i in range(0,len(aiHandP)):
                    if aiHandP[i][0] > max:
                        max = aiHandP[i][0]
                        maxID = i
                    if aiHandP[i][0] < min:
                        min = aiHandP[i][0]
                        minID = i
                if max < lead[0]: #Return smallest on suit if can't win
                    aiField = aiHandP.pop(minID)
                else: #Return highest on suit if can win
                    aiField = aiHandP.pop(maxID)
            else:
                offSuit = True
        else:
            print(f"-ERROR- The suit {lead[1]} doesn't exist somehow??")
        while offSuit == True:
            suit = random.randint(0, 3)
            if suit == 0 and len(aiHandD) != 0:
                randHand = aiHandD
            elif suit == 1 and len(aiHandS) != 0:
                randHand = aiHandS
            elif suit == 2 and len(aiHandF) != 0:
                randHand = aiHandF
            elif suit == 3 and len(aiHandP) != 0:
                randHand = aiHandP
            elif len(aiHandD) != 0:
                randHand = aiHandD
            elif len(aiHandS) != 0:
                randHand = aiHandS
            elif len(aiHandF) != 0:
                randHand = aiHandF
            elif len(aiHandP) != 0:
                randHand = aiHandP
            
            #Look for a small one so it isn't wasted
            min = 100
            minID = -1
            for i in range(0,len(randHand)):
                if min > randHand[i][0]:
                    min = randHand[i][0]
                    minID = i
            aiField = randHand.pop(minID)
            offSuit = False
        return aiField
    
    #-----Player is following-----
    else:
        mustFollow = False
        for i in range(0, len(playerHand)):
            if playerHand[i][1] == lead[1]:
                mustFollow = True

        displayHand(playerHand)
        print(f"\nCPU has played the {lead[0]} of {lead[1]}")
        tryLoop = True
        while tryLoop == True:
            try:

                validChoice = False

                #WHile look to ensure the player is picking an on suit card
                while validChoice == False:
                    choice = int(input("What card # would you like to play? "))

                    #If player has one or more on suit card and doesn't play one
                    if playerHand[choice][1] != lead[1] and mustFollow == True:
                        print(f"INVALID MOVE: Must follow when possible.  Play a different card with the [{lead[1]}] suit")
                        input("Press [ENTER] to continue: ")
                    
                    #Otherwise break out of the loop and play the choie
                    else:
                        validChoice = True

                #Set player field to your choice.  Pop said card out of the hand
                playerField = playerHand.pop(choice)
                tryLoop = False

            #When invalid card played (out of bounds or non number entry)
            except:
                input("\n\nERROR IN followTrick: Please enter a valid number from the list [press ENTER to continue] ")
        
        #Return the player Field
        return playerField

def scoreTrick(lead, follow, leader):
    '''Return true if leading player wins the trick.  Return false if leading player lost the trick'''
    if leader == True:
        print(f"\nYou led with the {lead[0]} of {lead[1]}")
        print(f"The AI followed with the {follow[0]} of {follow[1]}")
    else:
        print(f"\nThe AI led with the {lead[0]} of {lead[1]}")
        print(f"You followed with the {follow[0]} of {follow[1]}")

    if lead[1] == follow[1]: #following player played on suit
        if lead[0] >= follow[0]: #leading player had higher value
            if leader == True:
                print("\n\tYou won the trick!")
                return True
            else:
                print("\n\tYou lost the trick! [lower number]")
                return False
        else: #leading player had lower value
            if leader == True:
                print("\n\tYou lost the trick.. [lower number]")
                return False
            else:
                print("\n\tYou won the trick!")
                return True
    else:
        if leader == True:
            print("\n\tYou won the trick [Opponent played off suit]")
            return True #ai played off suit
        else:        
            print("\n\tYou lost the trick [played off suit]")
            return False #player played off suit

def lenAIHand():
    aiLength = len(aiHandD) + len(aiHandS) + len(aiHandF) + len(aiHandP)
    return aiLength

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

playerField = []
playerNum = -1 #This is where the following card goes
playerSuit = ""
playerLeading = True
playerShield = 0
playerTricks = 0


aiHand = []
aiHandD = []
aiHandS = []
aiHandF = []
aiHandP = []
aiHealth = 0
aiShield = 0
aiTricks = 0

aiField = []
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

#Reset gamestats :)))
deck = decklist.copy()
random.shuffle(deck)
draw(10, playerHand)
draw(10, aiHand)
playerHealth = 20
aiHealth = 20
playerTricks = 0
aiTricks = 0

#Game Loop
while len(playerHand) > 0 and lenAIHand() > 0:

    #AI leading Loop
    if playerLeading == False:
        aiField = leadTrick(playerLeading)
        playerField = followTrick(aiField,playerLeading)
        playerLeading = scoreTrick(aiField,playerField,playerLeading)

        #Powers go here (ai WAS leading)
        if playerLeading == False: #CPU was leading and won
            if aiField[1] == "Daggers":
                
                #Attack step
                attack = aiField[0]
                if playerField[1] == "Daggers": #If opponent plays on suit, reduce damage taken
                    attack -= playerField[0] 
                   
                    #If same value played, opponent doesn't reduce damage
                    if attack == 0: 
                        attack = aiField[0]
                
                #Opponent doesn't have shield
                if playerShield <= 0:
                    print(f"\n\CPU has dealt {attack} damage!")
                    playerHealth -= attack
                    print(f"\tYou are now at {playerHealth}HP.")
                
                #If they have shield, deal that much damage to shield, overspill does not trample to HP
                else:
                    print("\n\tThe opponent blocked the attack!")
                    playerShield -= attack
                    if playerShield < 0:
                        playerShield = 0

            #Create shield.  No opponent interaction here
            elif aiField[1] == "Shields":
                print(f"\n\tCPU gains {aiField[0]} shield points!")
                aiShield += aiField[0]
                print(f"\tCPU now has {aiShield} shield points.")

            #Feathers, draw 2
            elif aiField[1] == "Feathers":
                print("\n\tCPU nimbly dodges away! They draw 2 cards")
                draw(2, aiHand)
            
            #Potions: Gain HP.  That's it
            elif aiField[1] == "Potions":
                print("\n\tCPU takes a healing potion!")
                print(f"\tThey heal {aiField[0]}HP.")
                aiHealth += aiField[0]
                print(f"\tThey now have {aiHealth}HP")
        
        #Weak attack (leader lost the trick)
        else: 
            weakAtk = playerField[0] - 3
            if weakAtk <= 0:
                weakAtk = 1
            aiHealth -= weakAtk
            print(f"\n\tYour deal {weakAtk} damage")
            print(f"\tCPU is now at {aiHealth}")
    
    #Player leading Loop
    else:
        playerField = leadTrick(playerLeading)
        aiField = followTrick(playerField,playerLeading)
        playerLeading = scoreTrick(playerField, aiField, playerLeading)

        #Powers go here (player WAS leading)
        if playerLeading == True: #player was leading and won
            if playerField[1] == "Daggers":
                
                #Attack step
                attack = playerField[0]
                if aiField[1] == "Daggers": #If opponent plays on suit, reduce damage taken
                    attack -= aiField[0] 
                   
                    #If same value played, opponent doesn't reduce damage
                    if attack == 0: 
                        attack = playerField[0]
                
                #Opponent doesn't have shield
                if aiShield <= 0:
                    print(f"\n\tYou have dealt {attack} damage!")
                    aiHealth -= attack
                    print(f"\tCPU is now at {aiHealth}HP.")
                
                #If they have shield, deal that much damage to shield, overspill does not trample to HP
                else:
                    print("\n\tThe opponent blocked the attack!")
                    aiShield -= attack
                    if aiShield < 0:
                        aiShield = 0

            #Create shield.  No opponent interaction here
            elif playerField[1] == "Shields":
                print(f"\n\tYou gain {playerField[0]} shield points!")
                playerShield += playerField[0]
                print(f"\tYou now have {playerShield} shield points.")

            #Feathers, draw 2
            elif playerField[1] == "Feathers":
                print("\n\tYou nimbly dodge away! Draw 2 cards")
                draw(2, playerHand)
            
            #Potions: Gain HP.  That's it
            elif playerField[1] == "Potions":
                print("\n\tYou take a healing potion!")
                print(f"\tYou heal {playerField[0]}HP.")
                playerHealth += playerField[0]
                print(f"\tYou now have {playerHealth}HP")
        
        #Weak attack (leader lost the trick)
        else: 
            weakAtk = aiField[0] - 3
            if weakAtk <= 0:
                weakAtk = 1
            playerHealth -= weakAtk
            print(f"\n\tCPU player deals {weakAtk} damage")
            print(f"\tYou are now at {playerHealth}")


    #Tricks won (for tie breaker?)
    if playerLeading == True:
        playerTricks += 1
    elif playerLeading == False:
        aiTricks += 1

    #Win by Damage
    if playerHealth <= 0:
        print("\n\n\tYou have run out of HP.")
        break #I KNOW THIS IS BAD BUT THIS FELT CLEANER THAN HAVING AN ABOMINATION OF A WHILE LOOP THAT CHECKED FOR BOTH HAND SIZE AND ALSO HP
    elif aiHealth <= 0:
        print("\n\n\tCPU has run out of HP")
        break

    #Game end by empty hand
    if lenAIHand() == 0:
        print(f"\n\n\tCPU is out of cards. You deal a final {len(playerHand)} damage to them")
        aiHealth -= len(playerHand)
        if aiHealth < 0:
            aiHealth = 0
    if len(playerHand) == 0:
        print(f"\n\n\tYou are out of cards.  CPU deals a final {lenAIHand()} damage to you")
        playerHealth -= lenAIHand()
        if playerHealth < 0:
            playerHealth = 0

#Winner message
if playerHealth > aiHealth:
    winner = "you!"
elif playerHealth < aiHealth:
    winner = "the AI.."
else:
    winner = "nobody.  You tied the game :O"

#Won through message
if playerHealth > 0 and aiHealth > 0:
    cause = "through out maneuvering their opponent"
else:
    cause = "by destroying their opponent"
#Print Results
print("\n\n\t ~~Final Results~~")
print(f"You: {playerHealth}HP")
print(f" AI: {aiHealth}HP")
print(f"\nThe winner is {winner} {cause}")