from collections import deque


n, m = map(int, input().split())

graph = {}

for i in range(m):
    a,b = map(int, input().split())
    
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append([1, 0])
visited = set()
dist = -1

while len(q) > 0:
    starting, depth = q.popleft()
    visited.add(starting)
    
    if starting == n:
        dist = depth
        break
    
    for neighbor in graph[starting]:
        if neighbor not in visited:
            q.append([neighbor, depth+1])

print(dist - 1)