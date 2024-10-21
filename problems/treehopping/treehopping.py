from collections import deque
import sys

sys.setrecursionlimit(1000000)

def dfs(start, d):
    global parent, depth, graph, visited
    visited[start] = True
    for b in graph[start]:
        if not visited[b]:
            parent[b] = start
            depth[b] = d+1
            dfs(b, d+1)
            visited[b] = True

n = int(input())

for i in range(n):
    x = int(input())
    graph = {}
    for _ in range(x-1):
        a,b = map(int, input().split())
        if a not in graph:
            graph[a] = set()
        graph[a].add(b)
        if b not in graph:
            graph[b] = set()
        graph[b].add(a)
    
    visited = [False]*(x+1)
    parent = [0]*(x+1)
    depth = [0]*(x+1)
    dfs(1, 0)
    # print(table, path)
    

    permut = [int(input()) for _ in range(x)]
    failed = False
    for j in range(1, x):
        a = permut[j-1]
        b = permut[j]
        moves = 0
        found = False
        for i in range(4):
            if a == b:
                found = True
                break
            if depth[a] <= depth[b]:
                b = parent[b]
            elif depth[a] > depth[b]:
                a = parent[a]
        if not found:
            failed = True
            print(0)
            break
    if not failed:
        print(1)
    