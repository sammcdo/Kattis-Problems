n, m, k = map(int, input().split())

graph = {i:set() for i in range(1,n+1)}

for i in range(m):
    a,b = map(int, input().split())
    graph[a].add(b)

# make a blacklist of people who do not mutually like each other
blacklist = set()
for a in range(1,n+1):
    for b in graph[a]:
        if a not in graph[b]:
            blacklist.add(a)
            blacklist.add(b)

visited = set()
SCCs = [] # collection of Strongly Connected Components
for a in range(1,n+1):
    # already checked
    if a in blacklist or a in visited:
        continue

    found = True
    # y is the potential SCC
    y = set([i for i in graph[a]]+[a])
    # no blacklisted people allowed in a good SCC
    if y.intersection(blacklist):
        found = False
    
    # make sure all nodes in SCC also like each other
    for b in graph[a]:
        if b in blacklist:
            found = False
        x = y.intersection(graph[b])
        # print(b, x)
        if len(x) != len(graph[b]):
            found = False
    
    # update list of SCCs and visited
    if found:
        SCCs.append(a)
    visited.update(graph[a])

# find valid SCCs
count = 0
for i in SCCs:
    if len(graph[i])+1 == k:
        count += 1

print(count)