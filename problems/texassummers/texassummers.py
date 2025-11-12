from heapq import heappush, heappop
import math

n = int(input())

def calc_distance(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

stops = [[int(i) for i in input().split()] for _ in range(n)]
start = [int(i) for i in input().split()]
end = [int(i) for i in input().split()]

stops = [start, *stops, end]

# print(stops)

graph = {}


for node in range(len(stops)):
    graph[node] = []
    # for i in range(len(stops)):
    #     if calc_distance(stops[i], stops[n+1]) < calc_distance(stops[node], stops[n+1])**2:
    #         graph[node].append((i, calc_distance(stops[node], stops[i])**2))
    graph[node] = [(i, calc_distance(stops[node], stops[i])) for i in range(len(stops)) if node != i ]

# for k, v in graph.items():
#     print(k, v)

def dijkstra(graph, start, end):
    dist = {node: float("inf") for node in graph.keys()}
    prev = {}
    dist[start] = 0
    prev[start] = -1
    pq = [(0, start)]
    processed = set()
    while pq:
        cost, node_a = heappop(pq)
        #You can remove this if if you want all distances from start
        if node_a == end:
            return cost, prev
        # if node_a in processed: continue
        # processed.add(node_a)
        if cost > dist[node_a]: continue

        for node_b, w in graph[node_a]:
            if dist[node_b] > cost + w:
                dist[node_b] = cost + w
                prev[node_b] = node_a
                heappush(pq, (dist[node_b], node_b))
    return 0, prev


d, prev = dijkstra(graph, n+1, 0)

x = prev[0]
used = 0
while x != n+1:
    used = 1
    print(x-1)
    x = prev[x]

if used:
    pass
else:
    print("-")