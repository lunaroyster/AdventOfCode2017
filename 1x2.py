import re
inputString = open('input/1.txt').read()
s = 0
l = len(inputString)
for i in range(l):
    if (inputString[i]==inputString[int(i+(l/2))%l]):
        s+=int(inputString[i])
        
print(s)