import sys
sys.setrecursionlimit(1_000_000)

n, m = map(int, input().split())

graph = {i:[] for i in range(n)}

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start, end = map(int, input().split())

postD = {i:[] for i in range(n)}

def dijkstra(graph, start, end):
    from heapq import heappush, heappop
    dist = {node: float("inf") for node in graph.keys()}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cost, node_a = heappop(pq)

        for node_b, w in graph[node_a]:
            if dist[node_b] > dist[node_a] + w:
                dist[node_b] = dist[node_a] + w
                heappush(pq, (dist[node_b], node_b))
                postD[node_b] = []
                postD[node_b].append((node_a,w))
            elif dist[node_b] == dist[node_a] + w:
                postD[node_b].append((node_a,w))
    return dist

# get dist from any to any using dijkstras
shortestDn = dijkstra(graph, start, end)

onPath = [False]*n
p = [end]
while p:
    i = p.pop()
    onPath[i] = True
    if i == start:
        continue
    for x,_ in postD[i]:
        if not onPath[x]:
            p.append(x)


# tarjans articulation points w dfs
visited = [False]*n
depth = [float('inf')]*n
low = [float('inf')]*n
artPoints = set()

def dfs(s, d):
    global low, visited, depth, artPoints
    visited[s] = True
    depth[s] = d
    low[s] = min(d,low[s])

    for next, w in graph[s]:
        if not onPath[next]:
            continue
        if not visited[next]:
            dfs(next, d+1)
            if low[next] >= depth[s]:
                artPoints.add(s)
            low[s] = min(low[s], low[next])
        else:
            low[s] = min(low[s], depth[next])

dfs(start, 0)
artPoints.add(start)
artPoints.add(end)

print(*sorted(artPoints))