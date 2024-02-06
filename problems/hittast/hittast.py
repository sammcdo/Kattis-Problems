import heapq


def dijkstra(graph, start):
    """
    Run dijkstra's shortest path for an adjacency list graph
    O(edges log(verts) )
    :param graph: Dict of graph in form graph[node] = [(next, cost) ... ]
    :param start: The node to start from
    :return: distances
    """
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
            neighbors = graph[current_min]  # neighbors look like [(next, cost), (next, cost)]
            for neighbor in neighbors:  # check all neighbors as cheapest option and add to heap
                tentative_value = dist[current_min] + neighbor[1]
                if tentative_value < dist[neighbor[0]]:
                    dist[neighbor[0]] = tentative_value
                    heapq.heappush(unvisited, (neighbor[0], dist[neighbor[0]]))

    return dist
    
nodes, edges = map(int, input().split())

lodging = {}

for i, cost in enumerate(input().split()):
    lodging[i+1] = int(cost)

alf = {i:[] for i in range(1, nodes+1)}
ben = {i:[] for i in range(1, nodes+1)}

for i in range(edges):
    a, b, a_cost, b_cost = map(int, input().split())

    alf[a].append([b, a_cost])
    alf[b].append([a, a_cost])

    ben[b].append([a, b_cost])
    ben[a].append([b, b_cost])

a_cost = dijkstra(alf, 1)
b_cost = dijkstra(ben, nodes)

minCost = float('inf')
for i in range(1, nodes+1):
    cost = a_cost[i] + b_cost[i] + lodging[i]

    minCost = min(minCost, cost)
print(minCost)