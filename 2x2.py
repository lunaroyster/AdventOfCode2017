import re
inputString = open('input/2.txt').read()
rows = inputString.split('\n')
checksum = 0
for row in rows:
    cells = map((lambda x: int(x)), row.split('\t'))
    for cell1 in cells:
        for cell2 in cells:
            if cell1 == cell2: continue
            if(cell1%cell2==0): checksum+=cell1/cell2
print(checksum)