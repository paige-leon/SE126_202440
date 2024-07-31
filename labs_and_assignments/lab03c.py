#Paige Leon
#Week 3 In Class Lab
#7/29/24
#PROGRAM PROMPT:Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. 
#He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  
#Store the data from the file lab3a.csv into lists. Then process the lists to reprint all of the file information (exactly as you did in Lab 2) 
#and also produce an end report that lists the number of desktops that will be replaced,
#the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.


#Variable Dictionary
#-----------------------------------
#records = 0

#device = []
#brand = []
#cpu = []
#ram = []
#disk_one = []
#disk_two = []
#disk_num = []
#os = []
#yr = []

#cost   float

#---Imports---------------
import csv

#---Main Code-------------

#initialize variable that will count total # of records
records = 0
cost = 0

#create empty lists
device = []
brand = []
cpu = []
ram = []
disk_one = []
disk_two = []
disk_num = []
os = []
yr = []

with open("labs_and_assignments/lab3a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #update the records value
        records += 1

        #adding data to lists -> .append()
        if rec[0] == "D":
            device.append("Desktop")
        elif rec[0] == "L":
            device.append("Laptop")
        else:
            device.append("-DEVICE ERROR-")

        if rec[1] == "GW":
            brand.append("Gateway")
        elif rec[1] == "HP":
            brand.append("HP")
        elif rec[1] == "DL":
            brand.append("Dell")
        else:
            brand.append("-BRAND ERROR-")

        cpu.append(rec[2])
        ram.append(rec[3])
        disk_one.append(rec[4])
        disk_num.append(int(rec[5]))

        if int(rec[5]) == 1:
            disk_two.append("---")
            os.append(rec[6])
            yr.append(rec[7])
        elif int(rec[5]) == 2:
            disk_two.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])
        else:
            disk_two.append("-Error ")
            os.append(" @ ")
            yr.append(f"rec# {records}-")

#process the list(s) to view their storage
for i in range(0, records): #<--- goes from zero to records minus one
    print(f"{device[i]:10}\t{brand[i]:10}\t{cpu[i]:10}\t{ram[i]:10}\t{disk_one[i]:10}\t{disk_num[i]:10}\t{disk_two[i]:10}\t{os[i]:10}\t{yr[i]:10}\t")
    if int(yr[i]) <= 16:
        if device[i] == "Desktop":
            cost += 2000
        elif device[i] == "Laptop":
            cost += 1500

print(f"\n\n\tIt will cost ${cost:.2f} to replace the old computers")
