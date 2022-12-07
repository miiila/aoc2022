# Part 1
with open("./day6_input") as f:
    row = f.readline().strip()
    for i in range(0, len(row)):
        if len(set(row[i:i+4])) == 4:
            print(i+4)
            break

# Part 2
with open("./day6_input") as f:
    row = f.readline().strip()
    for i in range(0, len(row)):
        if len(set(row[i:i+14])) == 14:
            print(i+14)
            break
