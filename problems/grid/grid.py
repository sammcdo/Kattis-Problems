def bfs(graph, source, rows, cols):
    """
    Find a node in a graph
    :param graph: An adjacency list stored in a dict: graph[start] = [list of destination nodes]
    :param source: starting node
    :param target: destination node
    :return: whether it is in the graph
    """
    from collections import deque
    visited = {}
    queue = deque()
    found = False

    visited[source] = True
    queue.append([source, 0])

    while len(queue) > 0:          # Creating loop to visit each node
        m, moves = queue.popleft()

        i, j = m

        jump = graph[i][j]
        neighbors = []
        if i + jump < rows:
            neighbors.append((i+jump, j))
        if i - jump >= 0:
            neighbors.append((i-jump, j))
        if j + jump < cols:
            neighbors.append((i, j+jump))
        if j - jump >= 0:
            neighbors.append((i, j-jump))


        for neighbor in neighbors:
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append([neighbor, moves+1])
                if neighbor == (rows-1, cols-1):
                    found = True
                    break

        if found:
            return moves+1

    return -1

n, m = map(int, input().split())

graph = [[-1 for j in range(m)] for i in range(n)]


for i in range(n):
    x = input()
    for j in range(m):

        graph[i][j] = int(x[j])


moves = bfs(graph, (0,0), n, m)

print(moves)
