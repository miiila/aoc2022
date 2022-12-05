from copy import deepcopy
from collections import defaultdict

crates = defaultdict(list) 
instrunctions = []
with open("./day5_input") as f:
    parseInstructions = False
    for row in f.readlines():
        if parseInstructions:
            _, amount, _,fromm, _,to = row.split()
            instrunctions.append((int(amount), int(fromm), int(to)))
            continue
        j = 1
        for i in range(1, len(row), 4):
            ch = row[i]
            if ch != ' ' and ord(ch) > 64 :
                crates[j].append(row[i])
            j += 1
        if row == '\n':
            parseInstructions = True
            continue

# Part 1
crates1 = deepcopy(crates)
for amount, fromm, to in instrunctions:
    mv = list(reversed(crates1[fromm][0:amount]))
    crates1[to] = mv+crates1[to]
    crates1[fromm] = crates1[fromm][amount:] 

res = ''
for i in range(1,10):
    res = f'{res}{crates1[i][0]}'

print(res)

# Part 2
crates2 = deepcopy(crates) 
for amount, fromm, to in instrunctions:
    mv = crates2[fromm][0:amount]
    crates2[to] = mv+crates2[to]
    crates2[fromm] = crates2[fromm][amount:] 

res = ''
for i in range(1,10):
    res = f'{res}{crates2[i][0]}'

print(res)

