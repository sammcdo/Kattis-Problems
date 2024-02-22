import sys

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [0 for i in range(size)]

    def find(self, i):
        children = []
        while self.parent[i] != i:
            children.append(i)
            i = self.parent[i]
        for x in children:
            self.parent[x] = i
        return i

    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        isize = self.size[irep]
        jsize = self.size[jrep]
        if irep == jrep:
            return
        if isize < jsize:
            self.parent[irep] = jrep
            self.size[jrep] += isize
        else:
            self.parent[jrep] = irep
            self.size[irep] += jsize


n, q = map(int, sys.stdin.readline().split())

sets = UnionFind(n)

# for i in range(n):
#     sets.add(i)

for i in range(q):
    query, a, b = sys.stdin.readline().split()
    a, b = int(a), int(b)

    if query == "?":
        if sets.find(a) == sets.find(b):
            sys.stdout.write("yes\n")
        else:
            sys.stdout.write("no\n")
    else:
        sets.union(a, b)