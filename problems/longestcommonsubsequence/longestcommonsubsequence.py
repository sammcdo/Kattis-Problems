n, m = map(int, input().split())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = alpha[0:m]

counts = [[0] * m for _ in range(m)]

words = [input() for _ in range(n)]

for i in range(n):
    seen = set()
    this = words[i]
    l = set(map(lambda x: ord(x)-ord('A'), letters))
    for c in this:
        c = ord(c) - ord("A")
        seen.add(c)

        for x in l - seen:
            counts[c][x] += 1


# for i in counts:
#     print(i)

graph = {i:[]for i in range(m)}
for i in range(m):
    for j in range(m):
        if counts[i][j] == n:
            if i not in graph:
                graph[i] = []
            graph[i].append(j)


final = -1
for i in range(m):
    q = [(i, 1)]
    best = -1
    while q:
        this, d = q.pop(-1)
        if d > best:
            best = d
        for n in graph[this]:
            q.append((n,d+1))
    if best > final:
        final = best

print(final)