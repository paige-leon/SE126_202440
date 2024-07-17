#Paige Leon
#Lab 01
#7/17/24
#PROGRAM PROMPT: Create a program that determines whether a meeting room has space for a # of people


#Variable Dictionary
#-----------------------------------
#cont           y or n       controls the main while loop
#trap           True         controls the try except while loop
#meetingName    String       completely useless, but the prompt asked for it
#capacity       int          capacity of room
#people         int          people in attendence
#roomStatus     int          difference between capacity and people

#---Functions-------------
def difference(ppl:int, maxCap:int):
    '''User inputs # of people and the capacity of the room.  Outputs the difference.  Negative denotes overbooking, positive denotes open space'''
    diff = maxCap - ppl

    return diff

def decision(response):
    '''Recieves a value and parses it as either a y to continue, or a n to stop.  Invalid entry recursively calls self as needed'''
    
    response = input("Would you like to continue? [y/n]: ").lower() #Take input and also make it lowercase

    if response == "y" or response == "n": #Valid entry
        return response
    
    else: #Invalid entry
        print("\t\t***INVALID ENTRY***")
        return decision(response)
    
#---Main Code-------------


cont = "y"
while cont == "y": #------------Main Loop----------------

    meetingName = input("Enter the name of the meeting: ")
    
    trap = True #Trap loop-----------------------
    while trap == True:
        try:
            capacity = int(input("Enter the maximum capacity of the room: "))
            people = int(input("How many people are attending the meeting?: "))
            trap = False
        except:
            print("\n***INVALID ENTRY***\nCapacity and People in attendance MUST be a whole number")
    #------End Trap Loop-------------------

    roomStatus = difference(people, capacity)
    if roomStatus > 0: #1 or more spaces available
        print(f"\n\n\tYou have {roomStatus} open spots available for your meeting.")

    elif roomStatus < 0: #Meeting overbooked
        print(f"\n\n\tYour meeting is overbooked! You must remove {abs(roomStatus)} people.")

    else: #Exactly enough space
        print(f"\n\n\tThe roomed is packed to capacity. You are okay, but there are no more available seats.")
    
    #Continue?
    cont = decision(cont)

#-------End Main Loop----------------------
print("\n\nThank you for using the meeting calculator.  Goodbye :3") #ending message