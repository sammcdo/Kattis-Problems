from collections import deque
class MaxDistTree:
    """
    DFS to find deepest node from arbitrary start to find a diameter
    DFS from there to find other end of diameter
    BFS from one side of diameter to get distance
    BFS from other side of diameter to get distance
    """
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
    
    def bfs(self, start):
        self.visited = set()
        q = deque([(start,0)])
        dist = {start:0}
        farthest = (start, 0)
        while q:
            u, d = q.popleft()
            self.visited.add(u)
            for v in self.graph[u]:
                if v not in dist:
                    dist[v] = d+1
                    q.append((v,d+1))
                    if dist[v] > farthest[1]:
                        farthest = (v,d+1)
        return dist, farthest[0]
    
    def findDiameterLookups(self, start):
        _, self.d1 = self.bfs(start)
        self.d1L, self.d2 = self.bfs(self.d1)
        self.d2L, _ = self.bfs(self.d2)

n, q = map(int, input().split())

graph = {i:[] for i in range(1,n+1)}
for i in range(n-3):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

all = set(range(1,n+1))
islandA = MaxDistTree(graph)
islandA.findDiameterLookups(1)
left = all - islandA.visited

islandB = MaxDistTree(graph)
start = left.pop()
islandB.findDiameterLookups(start)
left = left - islandB.visited

islandC = MaxDistTree(graph)
start = left.pop()
islandC.findDiameterLookups(start)

islands = [islandA, islandB, islandC]

for i in range(q):
    a,b = map(int, input().split())

    x = [i for i in islands if a in i.visited][0]
    y = [i for i in islands if b in i.visited][0]
    z = [i for i in islands if i != x and i != y][0]

    val = max(x.d1L[a], x.d2L[a])+1 # longest route from a on its island
    val += z.d1L[z.d2]+1            # longest route on remaining island
    val += max(y.d1L[b], y.d2L[b])+1# longest route from b on its island

    print(val)
    