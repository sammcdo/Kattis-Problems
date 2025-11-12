from heapq import *

n, e = map(int, input().split())

graph = {i:[] for i in range(n)}

for i in range(e):
    a,b,w = map(int, input().split())
    graph[a].append((b,w,i))
    graph[b].append((a,w,i))

distance = [float('inf')]*n
distance[0] = 0
count = [0]*n
count[0] = 1
visited = set()
# print(distance)
q = [(0,0),]
heapify(q)
# print(q)
while len(q):
    x = heappop(q)
    w, start = x[0], x[1]
    # break
    if start in visited:
        continue
    visited.add(start)

    for nei, nw, _ in graph[start]:
        if distance[start]+nw < distance[nei]:
            distance[nei] = distance[start]+nw
            count[nei] = count[start]
            heappush(q, (distance[nei], nei))
        # elif distance[start]+nw == distance[nei]:
        #     count[nei] += count[start]
        #     heappush(q, (nw, nei))

# print(distance)
# print(count)
q = [(n-1, 0)]
edges = set()
visited = set()
totalTrail = 0
while q:
    start, dist = q.pop(-1)

    for nei, nw, id in graph[start]:
        if id not in edges:
        # print(start, nei, dist, distance[-1]-dist)
            if distance[-1]-dist-nw == distance[nei]:
                edges.add(id)
                totalTrail += nw
                q.append((nei, distance[-1]-distance[nei]))

# print(edges)
print(totalTrail*2)
