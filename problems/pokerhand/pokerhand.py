cards = input().split()

d = {}

for i in cards:
    if i[0] not in d:
        d[i[0]] = 0
    d[i[0]] += 1

m = 0
for k,v in d.items():
    if v > m:
        m = v
print(m)