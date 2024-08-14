#Comparing searching methods

import csv

#create empty lists
id = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open("demos_and_review/in_class_demos/w5_demoFile.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        id.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])
#disconnected
   
print(f"{"ID#":5}\t{"Last":15}\t{"First":15}")
print("===================================")
for i in range(0, len(id)):
    print(f"{id[i]:5}\t{lname[i]:15}\t{fname[i]:15}")
print("-----------------------------------")

#SEARCHING: always get the search item (query) FIRST
#SEQUENTIAL SEARCH -- "Searching in sequence" (from begging to end [or break])

search_name = input("Enter the LAST NAME you are looking for: ")
found = -1
seq_count = 0 #just tells us how many iterations it takes
br_count = 0
#For loop to check each value
for i in range(0,len(lname)):
    seq_count += 1
    if lname[i].lower() == search_name.lower(): #force lower so not case sensitive
        
        #store found value's location
        found = i

print(f"\n\tSequential Search Complete. Loop ran {seq_count} iterations.")
if found != -1:
    print(f"We found {search_name} at index {found}")
    print(f"Here is their info")

    print(f"{id[found]:5}\t{lname[found]:15}\t{fname[found]:15}")
else:
    print(f"could not find {search_name}")


#BINARY SEARCH -- take an ordered list and divide into 2 sections (high, low) and based on a MIDDLE will continually halve the search pool until a UNIQUE value is found (or isn't)
min = 0
max = len(lname) - 1
mid = int((min + max) / 2) #convert to int so it won't get decimals

bin_count = 0

#algy timmme!
while (min < max and search_name.lower() != lname[mid].lower()):
    bin_count += 1
    if search_name.lower() < lname[mid].lower():
        max = mid - 1 #mid is new max
    else:
        min = mid + 1 #mid is new min

    mid = int((min + max) / 2)

print(f"\n\tBinary Search Complete. Loop ran {bin_count} iterations.")
if search_name.lower() == lname[mid].lower():

    print(f"We found {search_name} at index {mid}")
    print(f"Here is their info")

    print(f"{id[mid]:5}\t{lname[mid]:15}\t{fname[mid]:15}")
else:
    print(f"could not find {search_name}")