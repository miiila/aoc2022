#      me
# them  R P S
#   R  3 6 0
#   P  0 3 6
#   S  6 0 3
rules = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3],
]

themOpts = ["A", "B", "C"]
meOpts = ["X", "Y", "Z"]

# Part 2
score = 0
with open("./day2_input") as f:
    for row in f.readlines():
        them, me = row.strip().split()
        them, me = themOpts.index(them), meOpts.index(me)
        score += me + 1 + rules[them][me]

print(score)

# Part 2
score = 0
with open("./day2_input") as f:
    for row in f.readlines():
        them, me = row.strip().split()
        them = themOpts.index(them)
        myScore = meOpts.index(me) * 3
        score += myScore + rules[them].index(myScore) + 1

print(score)
