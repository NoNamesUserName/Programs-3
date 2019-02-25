"""
Noah 
Rivera

Block 1
CompS2
"""

"""
Random.py
a program that generates 
25 numbers between 
1 and 100, and write them 
out to a file called random.txt
"""




import random
file=open("random.txt","w")
for i in range (25):
#used for random
#numbers and
#skiping to next line
   file.write(str(random.randint(1,100))+"\n")
file.close()
input("\n\nPress the enter key to exit."
