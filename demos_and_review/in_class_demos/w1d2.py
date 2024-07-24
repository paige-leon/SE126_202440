def converter(f):
    '''This function is passed a temp F value, converts to C and returns'''
    c = (f - 32) * (5/9)
    return c

tempCount = 0 #will hold sum total of all F temps
tempSum = 0 #will hold total number of all F temps entered
degree = u'\N{DEGREE SIGN}'
answer = "y"

print("Welcome to my Fahrenheit to Celsius Conversion Program!")

while answer == "y" or answer == "yes":

    tempF = float(input("\t\tEnter temperature in Fahrenheit: "))

    tempCount += 1
    tempSum += tempF

    #convert F to C --> use a function which returns a value
    tempC = converter(tempF)

    print(f"\t\t Temperature: {tempF:.1f}{degree}F | {tempC:.1f}{degree}C")

    #build a way out
    answer = input(f"You have entered {tempCount} temperatures.  Would you like to enter another? (y/n): ")
    answer = answer.lower() #make input lower case so user input is not case sensitive

    #Error Trap
    while answer != "y" and answer != "yes" and answer != "n" and answer != "no":
        print("\t\t***INVALID ENTRY***")
        answer = input("Would you like to enter another temp? [y/n]: ")

if tempCount != 0:
    tempAvg = tempSum / tempCount
    avgC = converter(tempAvg)

    print(f"\n\nYou have entered {tempCount} temperatures for an average of {tempAvg:.1f}{degree}F | {avgC:.1f}{degree}C")
else:
    print("You did not enter any temperatures :(")
print("\n\n\tOkay, bye, friend!\n\n")