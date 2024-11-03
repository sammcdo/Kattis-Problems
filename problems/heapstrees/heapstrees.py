import bisect
from collections import Counter

n = int(input())

graph = {i:[] for i in range(1,n+1)}

vals = {}

for i in range(1,n+1):
    v, p = map(int, input().split())
    vals[i] = v

    if p == 0:
        continue
    graph[p].append(i)

sets = {i:[] for i in range(0,n+1)}

for x in range(n, 0, -1):
    for next in graph[x]:
        if len(sets[x]) < len(sets[next]):
            sets[x], sets[next] = sets[next], sets[x]
        sets[x].extend(sets[next])
    sets[x].sort()

    p = bisect.bisect_left(sets[x], vals[x])
    if p >= len(sets[x]):
        sets[x].append(vals[x])
    else:
        sets[x][p] = vals[x]
    

print(len(sets[1]))