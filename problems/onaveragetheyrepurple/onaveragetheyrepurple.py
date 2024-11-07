from collections import deque

nodes, edges = map(int, input().split())

graph = {}

for i in range(edges):
    a,b = map(int, input().split())

    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start, target):
    q = deque()
    # [node, moves]
    q.append([start,0])
    visited = set()

    while len(q) > 0:
        # x = q.popleft()
        node, depth = q.popleft()
        visited.add(node)

        if node == target:
            return depth
        
        for next in graph[node]:
            if next not in visited:
                q.append([next, depth+1])


depth = bfs(graph, 1, nodes)

print(depth-1)
