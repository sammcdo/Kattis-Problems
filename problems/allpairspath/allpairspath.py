a,b,c = map(int, input().split())
graph = [[0 for j in range(150)] for i in range(150)]

while not (a==0 and b==0 and c==0):

    for i in range(a):
        for j in range(a):
            graph[i][j] = 0 if i == j else float('inf')

    for i in range(b):
        u, v, w = map(int, input().split())
        graph[u][v] = min(graph[u][v], w)

    V = a
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if graph[i][k] + graph[k][j] < graph[i][j] and graph[i][k] != float('inf') and graph[k][j] != float('inf'):
                    graph[i][j] = graph[i][k] + graph[k][j]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if graph[k][k] < 0 and graph[i][k] != float('inf') and graph[k][j] != float('inf'):
                    graph[i][j] = -float('inf')

    for i in range(c):
        u,v = map(int, input().split())

        if graph[u][v] == float('inf'):
            print("Impossible")
        elif graph[u][v] == -float('inf'):
            print("-Infinity")
        else:
            print(graph[u][v])
    print()

    a, b, c = map(int, input().split())