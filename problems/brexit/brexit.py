from collections import deque

def topo(graph, n, first):
    needed = [len(graph[i])/2 for i in range(n)]
    left = [False for i in range(n)]
    needed[first] = 0
    left[first] = True

    q = deque()
    q.append(first)

    # print(needed)


    while q:
        # print(q)
        m = q.popleft()
        for n in graph[m]:
            needed[n] -= 1
            if needed[n] <= 0 and left[n] == False:
                q.append(n)
                left[n] = True

    return left


c,p,x,l = map(int, input().split())
graph = {i:[] for i in range(c)}

for i in range(p):
    a,b = map(int, input().split())
    a -= 1
    b -= 1

    graph[a].append(b)
    graph[b].append(a)

# print(graph)

hasLeft = topo(graph, c, l-1)

if hasLeft[x-1]:
    print("leave")
else:
    print("stay")