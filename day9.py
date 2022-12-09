instructions = []
with open("./day9_input") as f:
# with open("./day9_input_test") as f:
    for row in f.readlines():
        row = row.strip().split()
        instructions.append((row[0], int(row[1])))

hpos = (0,0)
tpos = (0,0)
visited = set()

def tupleSub(a, b):
    return(a[0]-b[0], a[1]-b[1])

def tupleAdd(a, b):
    return(a[0]+b[0], a[1]+b[1])

def move(curPos, d):
    if d == 'D':
        return (curPos[0], curPos[1] - 1)
    if d == 'U':
        return (curPos[0], curPos[1] + 1)
    if d == 'R':
        return (curPos[0] + 1, curPos[1])
    if d == 'L':
        return (curPos[0] - 1, curPos[1])

# Part 1
for (d, l) in instructions:
    for _ in range(1,l+1):
        visited.add(tpos)
        hpos = move(hpos, d)
        diff = tupleSub(hpos, tpos)
        if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
            continue
        diff = (diff[0] if diff[0] == 0 else diff[0] // abs(diff[0]), diff[1] if diff[1] == 0 else diff[1] // abs(diff[1])) 
        tpos = tupleAdd(tpos, diff)
        visited.add(tpos)

print(len(visited))

# Part 2
visited = set()
hpos = (0,0)
tposs = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
for (d, l) in instructions:
    for _ in range(1,l+1):
        visited.add(tposs[8])
        hpos = move(hpos, d)
        h = hpos
        for i in range(0,len(tposs)):
            diff = tupleSub(h, tposs[i])
            if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
                h = tposs[i]
                continue
            diff = (diff[0] if diff[0] == 0 else diff[0] // abs(diff[0]), diff[1] if diff[1] == 0 else diff[1] // abs(diff[1])) 
            tposs[i] = tupleAdd(tposs[i], diff)
            h = tposs[i]
            visited.add(tposs[8])

print(len(visited))
