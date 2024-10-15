import heapq

def dijkstra(graph, start):
    global bonus
    """
    Run dijkstra's shortest path for an adjacency list graph
    O(edges log(verts) )
    :param graph: Dict of graph in form graph[node] = [(next, cost) ... ]
          Adjacency list of tuples
    :param start: The node to start from
    :return: distances
    """
    dist = {}  # stores the minimum distances
    maxVal = float('inf')
    for node in graph.keys():  # each distance preset to inf
        dist[node] = maxVal
    dist[start] = 0  # distance to start set to 0

    b = {}
    b[start] = bonus[start]
    included = {}
    included[start] = set([start])

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
                    if neighbor[0] not in included[current_min]:
                        thisSet = included[current_min].copy()
                        thisSet.add(neighbor[0])
                        b[neighbor[0]] = b[current_min] + bonus[neighbor[0]]
                        included[neighbor[0]] = thisSet
                    heapq.heappush(unvisited, (neighbor[0], dist[neighbor[0]]))
                if tentative_value == dist[neighbor[0]]:
                    if neighbor[0] not in included[current_min]:
                        thisSet = included[current_min].copy()
                        thisSet.add(neighbor[0])
                        tent_bonus = b[current_min] + bonus[neighbor[0]]
                        if tent_bonus > b[neighbor[0]]:
                            b[neighbor[0]] = tent_bonus
                            included[neighbor[0]] = thisSet
                    heapq.heappush(unvisited, (neighbor[0], dist[neighbor[0]]))
    # print(dist)
    # print(b)
    # print(included)
    return dist, b


n = int(input())
bonus = [0] + [int(i) for i in input().split()]
visited = [False for _ in range(n+1)]

edges = int(input())

graph = {i:[] for i in range(1,n+1)}

for i in range(edges):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

outs, bonusGot = dijkstra(graph, 1)

# print(outs)
# print(bonusGot)

if n in outs and n in bonusGot:
    print(outs[n], bonusGot[n])
else:
    print("impossible")