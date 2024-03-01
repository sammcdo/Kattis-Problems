villages, roads, start, end = [int(i) for i in input().split()]

edges = []

for i in range(roads):
    edge = [int(x) for x in input().split()]

    if edge[3] == 2:
        edge[3] = 0
        edge.append(1)
    elif edge[3] == 1:
        edge[3] = 1
        edge.append(0)
    else:
        edge[3] = 0
        edge.append(0)

    edge[0] -= 1
    edge[1] -= 1

    edges.append(edge)

distance = []

for i in range(villages):
    distance.append([float("inf"), float("inf"), float("inf")])

distance[start-1] = [0,0,0] # l, s, t

for i in range(villages-1):
    for e in edges:
        a, b, l, s, t = e

        if distance[b][2] > distance[a][2] + t: # more titans
            x,y,z = distance[a]
            distance[b] = [x+l, y+s, z+t]
        if distance[b][2] == distance[a][2] + t: # same titans
            if distance[b][1] > distance[a][1] + s: # more shamans
                x, y, z = distance[a]
                distance[b] = [x + l, y + s, z + t]
            if distance[b][1] == distance[a][1] + s: # same shamans
                if distance[b][0] > distance[a][0] + l: # more distance
                    x, y, z = distance[a]
                    distance[b] = [x + l, y + s, z + t]

    for e in edges:
        b, a, l, s, t = e

        if distance[b][2] > distance[a][2] + t:  # more titans
            x, y, z = distance[a]
            distance[b] = [x + l, y + s, z + t]
        if distance[b][2] == distance[a][2] + t:  # same titans
            if distance[b][1] > distance[a][1] + s:  # more shamans
                x, y, z = distance[a]
                distance[b] = [x + l, y + s, z + t]
            if distance[b][1] == distance[a][1] + s:  # same shamans
                if distance[b][0] > distance[a][0] + l:  # more distance
                    x, y, z = distance[a]
                    distance[b] = [x + l, y + s, z + t]

if float("inf") in distance[end-1]:
    print("IMPOSSIBLE")
else:
    print(*distance[end-1])