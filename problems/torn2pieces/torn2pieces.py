n = int(input())

def walk(edges, current, destination):
    mostRecent = current[-1]
    for edge in edges:
        start, end = edge[0], edge[1]
        if mostRecent == end:
            end, start = start, end
        if mostRecent == start:
            if destination == end:
                return current + [end]
            next = edges.copy()
            next.remove(edge)
            next_tree = current + [end]
            result = walk(next, next_tree, destination)
            if len(result) != 0:
                return result
    return []

edges = set()
for i in range(n):
    l = input().split()

    for i in range(1, len(l)):
        if l[0] < l[i]:
            edges.add((l[0], l[i]))
        else:
            edges.add((l[i], l[0]))

start, dest = input().split()

edges = list(edges)

steps = walk(edges, [start], dest)
if len(steps) > 0:
    print(" ".join(steps))
else:
    print("no route found")
