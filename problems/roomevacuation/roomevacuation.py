from collections import deque

class FF:
    def __init__(self, nodes) -> None:
        # self.graph = [[0]*nodes for i in range(nodes)]
        self.rgraph = {i:set() for i in range(nodes)}
        # self.parent = [False] * nodes
        self.nodes = nodes
    
    def addEdge(self, a,b,w):
        # self.graph[a][b] = w
        if a not in self.rgraph:
            self.rgraph[a] = set()
        if b not in self.rgraph:
            self.rgraph[b] = set()
        self.rgraph[a].add((b,w))
        self.nodes = len(self.rgraph)
    
    def bfs(self, s, t):
        """ Version used by ford fulkerson"""
        visited = {i:False for i in self.rgraph.keys()}
        q = deque()
        q.append([s, float('inf')])
        visited[s] = True
        self.parent[s] = -1

        # Standard BFS Loop
        while q: # note, can just use parent instead of
            u, flow = q.popleft()
            for v, w in self.rgraph[u]:
                canFlow = w > 0
                # print(u, v, canFlow)
                if v not in visited:
                    visited[v] = False
                if visited[v] == False and canFlow:
                    q.append([v, min(flow, w)])
                    self.parent[v] = u
                    visited[v] = True
                    if v == t:
                        return min(flow, w)
        return 0
    
    def FordFulkerson(self, s,t):
        """ Get max flow from node s to t on O(v^2e) """
        self.parent = {i:-1 for i in self.rgraph.keys()}
        max_flow = 0
        while True:

            path_flow = self.bfs(s,t)
            if path_flow == 0:
                break
            v = t
            while v != s:
                u = self.parent[v]
                newEdges = set(i for i in self.rgraph[u] if i[0] != v)
                self.rgraph[u] = newEdges
                newEdges = set(i for i in self.rgraph[v] if i[0] != u)
                newEdges.add((u,path_flow))
                self.rgraph[v] = newEdges
                v = self.parent[v]

            max_flow += path_flow

        # Return the overall flow
        return max_flow
    
    def getEdgeFlow(self,a,b):
        return 1 if (a, 1) in self.rgraph[b] else 0
    
def getNodeName(turn, row, col):
    return turn * 10000000 + row * 100 + col

def inbounds(row, col, n, m):
    return row >= 0 and row < n and col >= 0 and col < m

n, m, t = map(int, input().split())

mat = []
for i in range(n):
    mat.append(list(input()))

graph = FF(1)

sink = (t+3,0,0)
source = (0,0,0)

for x in range(t+1):
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 'E':
                graph.addEdge(getNodeName(x+1,i,j), getNodeName(*sink), 1)
                graph.addEdge(getNodeName(x+2,i,j), getNodeName(*sink), 1)
            if x < t:
                moves = [(1,0),(-1,0),(0,1),(0,-1), (0,0)]
                for move in moves:
                    next = [x+2, i+move[0], j+move[1]]
                    if inbounds(next[1], next[2], n, m) and mat[next[1]][next[2]] != "#":
                        graph.addEdge(getNodeName(x+1,i,j), getNodeName(*next), 1)

for i in range(n):
    for j in range(m):
        if mat[i][j] == 'P':
            graph.addEdge(getNodeName(*source), getNodeName(1,i,j), 1)

# for k, v in graph.rgraph.items():
    # print(k, v)
print(graph.FordFulkerson(getNodeName(*source), getNodeName(*sink)))

