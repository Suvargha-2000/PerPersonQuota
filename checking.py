import os 
lines = set()

def createData(total) :
    lines = set()
    for i in total.readlines() : 
        i = i.strip("\n")
        val = i.split("-")[0].strip()
        lines.add(val.lower())
    return lines

with open("total.txt") as total : 
    for i in total.readlines() : 
        i = i.strip("\n")
        val = i.split("-")[0].strip()
        lines.add(val.lower())

spents = []
personalSpentDirectories = os.listdir("persons/spent")
for i in personalSpentDirectories : 
    with open("persons/spent/" + i , "r") as personSpending : 
        spending = createData(personSpending)
        personalTotals = 0
        spents += list(spending)

spents = set(spents)
print(spents.difference(lines))
# print(spents , lines)
