n, m = map(int, input().split())

# get the graph and the reversed graph
g = {i:[] for i in range(n)}
gr = {i:[] for i in range(n)}

# valid is the nodes with no out edges (aka leaves)
valid = [0] * n
for i in range(m):
    a,b = map(int, input().split())
    a,b = a-1, b-1
    g[a].append(b)
    gr[b].append(a)
    # print(a,b, valid)
    valid[a] += 1

# dfs up tree to get the length of best path from leaf
done = [0]*n
length = [0]*n
q = [i for i in range(n) if valid[i] == 0]
while q:
    start = q.pop()
    done[start] += 1
    if done[start] < valid[start]:
        continue
    for next in gr[start]:
        q.append(next)
        length[next] = max(length[next], length[start]+1)

# print(length)

maxDepth = max(length)
depth = [[0,0] for _ in range(maxDepth+1)]

# dfs on reverse tree to find best path and second best path
q = [(i,0) for i in range(n) if length[i] == maxDepth]
visited = set()
while q:
    start, d = q.pop()

    if start in visited:
        continue
    visited.add(start)

    for next in g[start]:
        if depth[d][0] < length[next] + 1:
            depth[d][1] = depth[d][0]
            depth[d][0] = length[next] + 1
        elif depth[d][1] < length[next] + 1:
            depth[d][1] = length[next] + 1
        if length[next] != length[start] - 1:
            continue
        q.append((next, d+1))

# print(depth)

ans = maxDepth
# ans equals min second best path plus i steps to get to that edge
for i in range(maxDepth+1):
    ans = min(i+depth[i][1], ans)
print(ans)