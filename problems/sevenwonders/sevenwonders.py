s = input()

d = {
    "T":0,
    "C":0,
    "G":0,
}

for l in s:
    d[l] += 1

tot = 0
for v in d.values():
    tot += v**2
tot += 7*min(d.values())
print(tot)