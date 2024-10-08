import heapq
import sys

sys.setrecursionlimit(1000000)

def dfs(start):
    global graph, worst, times, visited

    if start not in worst:
        worst[start] = times[start]
    else:
        worst[start] = max(times[start], worst[start])

    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            w = dfs(neighbor)
            worst[start] = max(worst[start], w)
        else:
            worst[start] = max(worst[start], worst[neighbor])
    visited.add(start)
    return worst[start]



def topo(graph, times):
    V = len(graph)
    # Vector to store indegree of each vertex
    indegree = [0] * (V+1)
    for i in range(1, V+1):
        for vertex in graph[i]:
            indegree[vertex] += 1

    # Queue to store vertices with indegree 0
    q = []
    for i in range(1, V+1):
        if indegree[i] == 0:
            heapq.heappush(q, (-times[i], i))

    result = []
    while q:
        _, node = heapq.heappop(q)
        result.append(node)
        # Decrease indegree of adjacent vertices as the current node is in topological order
        for adjacent in graph[node]:
            indegree[adjacent] -= 1
            # If indegree becomes 0, push it to the queue
            if indegree[adjacent] == 0:
                heapq.heappush(q, (-times[adjacent], adjacent))
    return result


n = int(input())
times = {}
indeg = {}
graph = {}
worst = {}
visited = set()

for i in range(n):
    ins = [int(i) for i in input().split()]
    time, _, ends = ins[0], ins[1], ins[2:]
    start = i+1
    if start not in graph:
        graph[start] = []
    for e in ends:
        if e not in graph:
            graph[e] = []
        graph[e].append(start)
    indeg[start] = len(ends)
    times[start] = time


for i in range(1, n+1):
    if indeg[i] == 0:
        dfs(i)

# print(worst)

# print(graph)
t = topo(graph, worst)
# print(t)

best = 0
for i in range(len(t)):
    x = t[i]
    thisTime = times[x] + i
    best = max(best, thisTime)

print(best)