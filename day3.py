import functools

# Part 1
with open("./day3_input") as f:
    res = 0
    for row in f.readlines():
        row = row.strip()
        half = len(row) // 2
        first, second = map(set, [row[0:half], row[half:]])
        score = ord(first.intersection(second).pop()) - 96
        if score < 0:
            score += 32 + 26
        res += score

print(res)

# Part 2
with open("./day3_input") as f:
    res = 0
    rows = [r.strip() for r in f.readlines()]

    for i in range(0, len(rows), 3):
        common = functools.reduce(set.intersection, [set(r) for r in rows[i : i + 3]])
        score = ord(common.pop()) - 96
        if score < 0:
            score += 32 + 26
        res += score

print(res)
