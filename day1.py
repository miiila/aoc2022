from sortedcontainers import SortedList

summ = 0
sl = SortedList()
with open('./day1_input') as f:
    for row in f.readlines():
        if row == '\n':
            sl.add(summ)
            summ = 0
        else:
            summ += int(row)
# First
print(sl[-1])
# Second
print(sl[-1]+sl[-2]+sl[-3])
