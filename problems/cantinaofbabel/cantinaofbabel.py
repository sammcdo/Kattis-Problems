from collections import deque

class SCC:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, source):
        visited = {}
        stack = deque()
        found = False

        visited[source] = True
        stack.append(source)

        while len(stack) > 0:  # Creating loop to visit each node
            m = stack.popleft()

            for neighbour in self.graph[m]:
                if neighbour not in visited:
                    visited[neighbour] = True
                    stack.append(neighbour)

        return visited

    def transpose(self):
        g = {}

        for i in self.graph:
            for j in self.graph[i]:
                if j not in g:
                    g[j] = [i]
                else:
                    g[j].append(i)
            if i not in g:
                g[i] = []

        return g

    def isSSC(self):
        s = list(self.graph.keys())[0]
        v1 = self.bfs(s)

        old = self.graph
        self.graph = self.transpose()

        v2 = self.bfs(s)

        self.graph = old

        if set(v1) == set(v2):
            return True
        else:
            return False

    def getSSC_Size(self, start):
        s = start
        v1 = set(self.bfs(s))

        old = self.graph
        self.graph = self.transpose()

        v2 = set(self.bfs(s))

        self.graph = old

        return len(v1.intersection(v2))



d = {}
s = {}
u = {}
n = []

total_size = int(input())

for i in range(total_size):
    words = input().split()
    name = words.pop(0)
    speaks = words.pop(0)
    understands = words

    if speaks not in s:
        s[speaks] = []
    s[speaks].append(name)

    for x in understands:
        if x not in u:
            u[x] = []
        u[x].append(name)

    if speaks not in u:
        u[speaks] = []
    u[speaks].append(name)

    n.append(name)

for people in n:
    d[people] = []

for lang, peoples in s.items():
    for person in peoples:
        if person not in d:
            d[person] = []

        for other in u[lang]:
            if other != person:
                if person not in d:
                    d[person] = []
                d[person].append(other)

connected = SCC(d)
largest = 0
for person in n:
    temp = connected.getSSC_Size(person)
    largest = max(temp, largest)

print(total_size - largest)


