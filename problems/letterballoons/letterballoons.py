l, n = map(int, input().split())

letters = [chr(i) for i in range(ord('A'),ord('A')+l)]

schools = set()

for i in range(n):
    x = [i for i in input()]
    x.sort()
    s = set(x)

    if len(s) < len(x) or x[-1] > letters[-1]:
        continue

    schools.add(tuple(x))

best = 0
for i in schools:
    used = set(letters)
    used -= set(i)
    x = 1
    for j in schools:
        if i == j:
            continue
        if set(j).issubset(used):
            used -= set(j)
            x += 1
    best = max(best, x)

print(best)