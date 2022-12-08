from copy import deepcopy
forest = []
with open("./day8_input") as f:
    for row in f.readlines():
        forest.append([int(tree) for tree in row.strip()])


# Part 1
visible = deepcopy(forest)
# left right
for r in range(0,len(forest)):
    limit = -1
    for c in range(0, len(forest[r])):
        if forest[r][c] > limit:
            visible[r][c] = 'x'
            limit = forest[r][c]

# right left
for r in range(len(forest)-1, -1,-1):
    limit = -1
    for c in range(len(forest[r])-1, -1, -1):
        if forest[r][c] > limit:
            visible[r][c] = 'x'
            limit = forest[r][c]

# top down
for c in range(0, len(forest[0])):
    limit = -1
    for r in range(0, len(forest)):
        if forest[r][c] > limit:
            visible[r][c] = 'x'
            limit = forest[r][c]

# bottom up
for c in range(len(forest[0]) -1, -1, -1):
    limit = -1
    for r in range(len(forest) -1, -1, -1):
        if forest[r][c] > limit:
            visible[r][c] = 'x'
            limit = forest[r][c]

res = 0
for row in visible:
    res += sum([1 for x in row if x == 'x']) 

print(res)

# Part 2
maxx = -1
for r in range(0,len(forest)):
    for c in range(0, len(forest[r])):
        curmax = 1
        #top
        s = 0
        for i in range(r-1, -1, -1):
            s += 1
            if forest[i][c] >= forest[r][c]:
                break
        curmax *= s 
        #right
        s = 0
        for i in range(c+1, len(forest[r])):
            s += 1
            if forest[r][i] >= forest[r][c]:
                break
        curmax *= s
        #down
        s = 0
        for i in range(r+1, len(forest)):
            s += 1
            if forest[i][c] >= forest[r][c]:
                break
        curmax *= s
        #left
        s = 0
        for i in range(c-1, -1, -1):
            s += 1
            if forest[r][i] >= forest[r][c]:
                break
        curmax *= s

        maxx = max(maxx, curmax)

print(maxx)




