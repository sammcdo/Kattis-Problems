from collections import deque
class FF:
    def __init__(self, nodes) -> None:
        # self.graph = [[0]*nodes for i in range(nodes)]
        self.rgraph = {i:set() for i in range(nodes)}
        # self.parent = [False] * nodes
        self.nodes = nodes
    
    def addEdge(self, a,b,w):
        # self.graph[a][b] = w
        self.rgraph[a].add((b,w))
    
    def bfs(self, s, t):
        """ Version used by ford fulkerson"""
        visited = [False] * self.nodes
        q = deque()
        q.append([s, float('inf')])
        visited[s] = True
        self.parent[s] = -1

        # Standard BFS Loop
        while q: # note, can just use parent instead of visited
            u, flow = q.popleft()
            for v, w in self.rgraph[u]:
                canFlow = (v, 1) in self.rgraph[u]
                if visited[v] == False and canFlow:
                    q.append([v, min(flow, 1)])
                    self.parent[v] = u
                    visited[v] = True
                    if v == t:
                        return min(flow, 1)
        return 0
    
    def FordFulkerson(self, s,t):
        """ Get max flow from node s to t on O(v^2e) """
        self.parent = [-1] * self.nodes
        max_flow = 0
        while True:

            path_flow = self.bfs(s,t)
            if path_flow == 0:
                break
            v = t
            while v != s:
                u = self.parent[v]
                self.rgraph[u].discard((v,path_flow))
                self.rgraph[v].add((u,path_flow))
                v = self.parent[v]

            max_flow += path_flow

        # Return the overall flow
        return max_flow
    
    def getEdgeFlow(self,a,b):
        return 1 if (a, 1) in self.rgraph[b] else 0

n = int(input())

graph = {}
opts = []
used = {}
c = 0
for i in range(n):
    a,b = map(int, input().split())
    opts.append((a,b))
    graph[i] = [a+b, a-b, a*b]
    for i in graph[i]:
        if i not in used:
            used[i] = c
            c+=1

size = n+len(used.keys())+2
matrix = FF(size)
source = size-2
sink = size-1
for i in range(n):
    outs = graph[i]
    for j in outs:
        j = used[j]
        matrix.addEdge(i, j+n, 1)
        matrix.addEdge(j+n, sink, 1)
    matrix.addEdge(source, i, 1)

x = matrix.FordFulkerson(source, sink)
# print(x)

if x == n:
    for i in range(n):
        outs = graph[i]
        x,y,z = graph[i]
        if matrix.getEdgeFlow(i, n+used[x]) == 1:
            a,b = opts[i]
            print(a, "+", b, "=", a+b)
        elif matrix.getEdgeFlow(i, n+used[y]) == 1:
            a,b = opts[i]
            print(a, "-", b, "=", a-b)
        elif matrix.getEdgeFlow(i, n+used[z]) == 1:
            a,b = opts[i]
            print(a, "*", b, "=", a*b)
else:
    print("impossible")
    
    