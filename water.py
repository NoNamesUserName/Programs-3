"""
Noah
Rivera
"""

"""
Water.py

A small town in the California desert,
Dry Gulch has an underground water storage tank
that contains 10,000 gallons of water. Thankfully
(given that it's another drought season),
the tank has not been discovered by any nearby
golf courses, water parks, or mineral water companies,
and is still dedicated for use only by the residents of
Dry Gulch. Given an input file that contains weekly usage
rate for the town residents,
calculate the number of weeks the water will last.
"""
#tells you how many numbers there are by openin the file as a sting then reads how long the string is
i=0
file=open("water.txt","r")
countnums=file.readlines()
run=len(countnums)
file.close()
file=open("water.txt","r")
#tells you how many numbers there are by openin the file as a sting then reads how long the string is

# Reads the file and puts it into a variable to use for later
def water():
    amount=file.readline()
    return int(amount)
# Reads the file and puts it into a variable to use for later
used = open("usage.txt","w")
#print out original number to the file divides by 10,000 and goes to next line
for i in range (run-1):
    x=water()
    line = (str(x) + " gallons per week will last " + str(10000 //x) + " weeks\n")
    used.write(line)
file.close()
used.close()
input("\n\nPress the enter key to exit."

