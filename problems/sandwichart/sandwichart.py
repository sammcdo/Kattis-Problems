n,g,d,m = map(int, input().split())

curr = [int(i) for i in input().split()]
genres = []

for i in range(g):
    this = set([int(x) for x in input().split()])
    genres.append(this)

req = {}

for i in range(d):
    a,b = map(int, input().split())
    if a not in req:
        req[a] = set()
    req[a].add(b)

i = 0
c = set(curr)
while i < len(curr):
    dep = curr[i]
    if dep in req:
        for need in req[dep]:
            if need not in c:
                curr.append(need)
                c.add(need)
    i += 1

if len(curr) > m:
    print('disaster')
    exit(0)

for genre in genres:
    if c.issubset(genre):
        print('masterpiece')
        exit(0)

print('disaster')