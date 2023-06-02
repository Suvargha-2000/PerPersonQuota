import os
import math
import pandas as pd 

def createData(total) : 
    lines = []
    for i in total.readlines() : 
        i = i.strip("\n")
        val = i.split("-")
        for i in range(len(val)) : 
            val[i] = val[i].strip()
        val[-1] = int(val[-1])
        lines.append(val)
    return lines

with open("total.txt" , "r") as total : 
    totalData = createData(total)

total = 0 
persons = []
for i in totalData : 
    total += i[-1]

personalSpentDirectories = os.listdir("persons/spent")
personalRecvDirectories = os.listdir("persons/recieved")
personalSpendings = []
personalRecieving = {}

print("Total Spent on Trip : " , total)
print("Per Person Spent :" , math.ceil(total/len(personalSpentDirectories)))

perPersonSpendings = math.ceil(total/len(personalSpentDirectories))

for i in personalSpentDirectories : 
    with open("persons/spent/" + i , "r") as personSpending : 
        spending = createData(personSpending)
        personalTotals = 0
        for j in spending:
            print(j)
            personalTotals += j[-1]


    personalSpendings.append([ i.split(".")[0] ,personalTotals])

for i in personalRecvDirectories :
    with open("persons/recieved/" + i , "r") as personRecv :
        recv = createData(personRecv)
        personalTotals = 0
        for j in recv :
            personalTotals += j[-1]

    personalRecieving[i.split(".")[0]] = personalTotals

df = pd.DataFrame(personalSpendings)

print(personalRecieving)

df.rename(columns = {0:'Names'}, inplace = True)
df.rename(columns = {1:'Spendings'}, inplace = True)
df["Recieved"] = 0
df["Remaining"] = 0

for i in df.index : 
    if df["Names"][i] in personalRecieving :
        df["Recieved"][i] = personalRecieving[df["Names"][i]]


for i in df.index :
    try : 
        df["Remaining"][i] = perPersonSpendings - df["Spendings"][i] + personalRecieving[df["Names"][i]]
        print(df["Names"][i])
    except :
        df["Remaining"][i] = perPersonSpendings - df["Spendings"][i]

print(df)


