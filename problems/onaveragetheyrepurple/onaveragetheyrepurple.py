
def bfs(graph, source, target):
    """
    Find a node in a graph
    :param graph: An adjacency list stored in a dict: graph[start] = [list of destination nodes]
    :param source: starting node
    :param target: destination node
    :return: minimum nodes to visit (shortest path)
    """
    from collections import deque
    visited = {}
    queue = deque()

    visited[source] = 0
    queue.append(source)

    while len(queue) > 0:  # Creating loop to visit each node
        m = queue.popleft()
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited[neighbor] = 1 + visited[m]
                queue.append(neighbor)
                if neighbor == target:
                    return visited[m] + 1
    return -1

n, m = map(int, input().split())

graph = {}
for i in range(m):
    a, b = map(int, input().split())

    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

dist = bfs(graph, 1, n)

print(dist-1)