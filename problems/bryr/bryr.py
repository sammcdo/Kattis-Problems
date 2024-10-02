import heapq
def dijkstra(graph, start, target):
    #priority queue to explore the nodes with the smallest known distance first
    pq = [(0,start)] #(current distance, node)

    #distances dictionary intialized to infinity for all nodes:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0 #initialize the distance from start to itself to 0

    while pq:
        curr_distance, curr_node = heapq.heappop(pq)
        #return immediately if reached last node, target
        if curr_node == target:
            return curr_distance
        
        #if current distance is greater than recorded distance, continue
        if curr_distance > distances[curr_node]:
            continue

        #explore neighbor
        for neighbor, weight in graph[curr_node]:
            distance = curr_distance + weight

            #only proceed if this path is better (shorter)
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return float('inf')#exit without finding target, there is no path

import sys
data = []
for line in sys.stdin:
    int_array = list(map(int, line.split()))
    data.append(int_array)

# 3 -> 1 search for 3-key and put (1, 1) as format (neighbor, weight). I also need to add 1 -> 3 as (3, 1) since it's bidiretional
# graph = {
#     1: [(2,1), (3,1)],
#     2: [(3,1), (1,1)],
#     3: [(1,1)]
# }
graph = dict()

# initialize graph with num:[] for all the locations (first number in line 1)
for num in range(1, data[0][0]+1):
    graph[num] = []

# pass in and initialize distance from 1
for start,end,weight in data[1:]:
    graph[start].append((end,weight))
    graph[end].append((start,weight))

least_weight = dijkstra(graph, 1, data[0][0])
print(least_weight)