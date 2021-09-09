import csv
import os

os.system('cls')

f1 = open('dwarf_stars.csv')

csvo1 = csv.reader(f1)

data1 = []

for row in csvo1:
    data1.append(row)

header1 = data1[0]
DwarfStarData = data1[1:]

header1[0] = "Index"

tempList = list(DwarfStarData)
for d in tempList:
    if(d[4] == ''):
        DwarfStarData.remove(d)
    if(d[4] != ''):
        d[4] = float(d[4])*0.102763


tempList = list(DwarfStarData)
for d in tempList:
    if(d[3] == ''):
        DwarfStarData.remove(d)
    if(d[3] != ''):
        d[3] = float(d[3])*0.000954588

with open('DwarfStars.csv', 'w') as f:
    csvo = csv.writer(f)
    csvo.writerow(header1)
    csvo.writerows(DwarfStarData)
