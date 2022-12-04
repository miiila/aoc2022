# Part 1
with open("./day4_input") as f:
    res = 0
    for row in f.readlines():
        row = row.strip()
        elf1, elf2 = row.split(',')
        elf1, elf2 = elf1.split('-'), elf2.split('-')
        elf1, elf2 = [int(x) for x in elf1], [int(x) for x in elf2] 
        if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
            res += 1
    print(res)

# Part 2
with open("./day4_input") as f:
    res = 0
    for row in f.readlines():
        row = row.strip()
        elf1, elf2 = row.split(',')
        elf1, elf2 = elf1.split('-'), elf2.split('-')
        elf1, elf2 = [int(x) for x in elf1], [int(x) for x in elf2] 
        if (elf1[0] >= elf2[0] and elf1[0] <= elf2[1]) or (elf1[1] >= elf2[0] and elf1[1] <= elf2[1]) or (elf2[0] >= elf1[0] and elf2[0] <= elf1[1]) or (elf2[1] >= elf1[0] and elf2[1] <= elf1[1]):
            res += 1
    print(res)
