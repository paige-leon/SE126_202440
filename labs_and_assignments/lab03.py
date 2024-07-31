#Paige Leon
#Lab #03
#7/31/24
#PROGRAM PROMPT:
#Construct a program that will analyze potential voters. The program should generate the following totals:

#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.

#Variable Dictionary
#-----------------------------------
#processed          counts number of people checked
#ineligible         people under 18
#eligible           processed - ineligble
#not_registered     over 18, not registered
#no_vote            registered, didn't vote
#voted              registered, voted

#parallel lists, stores data from file
#id = []
#age = []
#is_registered = []
#votes = []

#Notes:
#variable eligible never actually gets used aside from counting I'm pretty sure.  I thought I'd need it and then didn't. oopsies.

#---Imports---------------
import csv

#---Main Code-------------


#initialize counters/empty lists
id = []
age = []
is_registered = []
votes = []

processed = 0
ineligible = 0
not_registered = 0
no_vote = 0
voted = 0

with open("labs_and_assignments/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        
        #incriment county boy
        processed += 1

        #make a bunch of parallel lists
        id.append(rec[0])
        age.append(int(rec[1]))
        is_registered.append(rec[2])
        votes.append(rec[3])
#close file

eligible = processed #set eligible voters to the number of processed people (for now :3)

for i in range(0, processed):
    
    #underage
    if age[i] < 18:
        ineligible += 1 #incriment ineligbile voters
        eligible -= 1 #decrease eligible voters for no reason

    #not registered
    elif is_registered[i].upper() == "N":
        not_registered += 1

    #didn't vote
    elif votes[i].upper() == "N":
        no_vote += 1

    #voted
    else:
        voted += 1


#Output
print("\nVoting registration data:")
print("===========================")
print(f"Too Young     |{ineligible:3}ppl")
print(f"Unregistered  |{not_registered:3}ppl")
print(f"Didn't Vote   |{no_vote:3}ppl")
print(f"Voted         |{voted:3}ppl")
print(f"Total         |{processed:3}ppl")
print("\n\n\tThank you, goodbye :3")