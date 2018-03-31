import sys
import random

mynum = []
inp = int(input("Enter your pw length: "))

allstr = 'A1bc23'

print("length of allstr = ", len(allstr))
print("range of inp")
print(range(inp))
print("start for loop")

for i in range(inp):
    print("i", i)
    thisnum = int(random.randint(0,len(allstr)))
    print("thisnum", thisnum)
    mynum.append(thisnum)
    print("mynum",mynum)

print("end for loop")
print("final mynum object is...", mynum)


#allstr[mynum]
pasw = ''
print("this is pasw", pasw)

for x in mynum:
    pasw = str(pasw) + str(allstr[x])

print("pasw", pasw)
