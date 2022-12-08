from collections import defaultdict
# Part 1
system = defaultdict(int)
dirs = defaultdict(list)
content = defaultdict(list)
with open("./day7_input") as f:
    currentDirs = []
    for row in f.readlines():
        row = row.strip()
        if row[0] == '$':
            if row[2:4] == 'cd':
                if row[5:7] == '..':
                    currentDirs.pop(-1)
                    continue
                else:
                    currentDirs.append(row[5:])
        else:
            if row[0:3] == 'dir':
                dirs['>'.join(currentDirs)].append(row[4:])
            else:
                content['>'.join(currentDirs)].append(row)

def calculateSizeRec(content, dirs, curDir):
    size = 0
    for dirr in dirs.get(curDir, []):
        size += calculateSizeRec(content, dirs, f'{curDir}>{dirr}')
    for file in content[curDir]:
        size += int(file.split()[0])
    system[curDir] = size

    return size
calculateSizeRec(content, dirs, '/')

res = sum([x for x in system.values() if x <= 100000])
print(res)

# Part 2
unused = 70000000 - system['/']
needed = 30000000 - unused
res = ([(name, val) for name, val in system.items() if val >= needed])
res.sort(key= lambda x: x[1])
print(res[0][1])
