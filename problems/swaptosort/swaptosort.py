n, m = map(int, input().split())

graph = [-1 for i in range(n)]


def find(graph, a):
    if graph[a] == -1:
        return a
    else:
        graph[a] = find(graph, graph[a])
        return graph[a]


def join(graph, a, b):
    a = find(graph, a)
    b = find(graph, b)

    if a != b:
        graph[a] = b


for i in range(m):
    a,b = map(lambda x: int(x)-1, input().split())

    join(graph, a, b)

found = True
for i in range(n):
    if find(graph, i) != find(graph, n-i-1):
        found = False


if found:
    print("Yes")
else:
    print("No")