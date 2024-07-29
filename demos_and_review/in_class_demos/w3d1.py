import csv

#initialize variable that will count total # of records
records = 0

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

with open("demos_and_review/in_class_demos/lab2b.csv") as csvfile:

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

