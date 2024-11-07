import sys, heapq, math

def dijkstra(graph, start):
    dist = {}  # stores the minimum distances
    maxVal = float('inf')
    for node in graph.keys():  # each distance preset to inf
        dist[node] = maxVal
    dist[start] = 0  # distance to start set to 0
    unvisited = []  # heap of unvisited nodes
    heapq.heappush(unvisited, (start, 0))  # init heap of form (node, cost)
    while unvisited:  # continue while unvisited nodes remain
        current_min, current_cost = heapq.heappop(unvisited)
        if current_cost == dist[current_min]:  # should be processing
            neighbors = graph[current_min]
            # neighbors look like [(next, cost), (next, cost)]
            for neighbor in neighbors:
            # check all neighbors as cheapest option and add to heap
                tentative_value = dist[current_min] + neighbor[1]
                if tentative_value < dist[neighbor[0]]:
                    dist[neighbor[0]] = tentative_value
                    heapq.heappush(unvisited, (neighbor[0], dist[neighbor[0]]))
    return dist

homeX, homeY, destX, destY = map(int, input().split())

subSpeed = 40*1000/60
walkSpeed = 10*1000/60

edges = []
lines = []
l = sys.stdin.readline()
while l:
    edges = []
    l = l.split()

    for i in range(0, len(l), 2):
        a, b = int(l[i]), int(l[i+1])
        if a == -1:
            break
        else:
            edges.append((a,b))

    lines.append(edges)
    l = sys.stdin.readline()

graph = {}
nodes = set()
for line in lines:
    for i in range(0, len(line)-1):
        n1 = line[i]
        n2 = line[i+1]

        if n1 not in graph:
            graph[n1] = []
        if n2 not in graph:
            graph[n2] = []

        dist_btw = ((n1[0] - n2[0])**2 + (n1[1] - n2[1])**2)**0.5

        graph[n1].append([n2, dist_btw/subSpeed])
        graph[n2].append([n1, dist_btw/subSpeed])
        nodes.add(n1)
        nodes.add(n2)

nodes.add((homeX, homeY))
nodes.add((destX, destY))

for i in nodes:
    for j in nodes:
        n1 = i
        n2 = j
        dist_btw = ((n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2) ** 0.5

        if n1 not in graph:
            graph[n1] = []
        if n2 not in graph:
            graph[n2] = []

        graph[n1].append([n2, dist_btw/walkSpeed])
        graph[n2].append([n1, dist_btw/walkSpeed])

dist = dijkstra(graph, (homeX, homeY))

print(round(dist[(destX, destY)]))
