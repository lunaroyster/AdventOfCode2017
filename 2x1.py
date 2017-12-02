import re
inputString = open('input/2.txt').read()
rows = inputString.split('\n')
checksum = 0
for row in rows:
    cells = map((lambda x: int(x)), row.split('\t'))
    checksum += max(cells) - min(cells)
print(checksum)