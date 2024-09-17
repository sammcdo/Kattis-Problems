from collections import deque

n, m = map(int, input().split())

graph = [[0 for i in range(m)] for j in range(m)]

for i in range(n):
    opts = [int(i) for i in input().split()][1::]
    for item in opts:
        graph[i][item-1] = 1

def dfs(graph, u, matchR, seen):
    for v in range(m):
        if graph[u][v] and seen[v] == False:
            seen[v] = True
            if matchR[v] == -1 or dfs(graph, matchR[v], matchR, seen):
                matchR[v] = u
                return True
    return False

def bpm(graph):
    matchR = [-1] * m
    result = 0
    for i in range(n):
        seen = [False] * m
        if dfs(graph, i, matchR, seen):
            result += 1
    return result

count = bpm(graph)

print(count)
