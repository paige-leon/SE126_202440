#W3D2 - Data from a text file to 1D parallel lists

import csv

records = 0

#make some empty boys to populate
names = []
ages = []
colors = []
animals = []

with open("demos_and_review/in_class_demos/classList_202140.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: #File is technically a 2D list :O
        #rec is a list of data representing 1 line of file.
        #file[0] is the first rec

        #incriment counter
        records +=1 

        names.append(rec[0])
        ages.append(int(rec[1]))
        colors.append(rec[2])
        animals.append(rec[3])

for i in range(0, records):
    print(f"{names[i]} is {ages[i]} years old.  Their favorite color is {colors[i]} and their favorite animal is the {animals[i]}.")
