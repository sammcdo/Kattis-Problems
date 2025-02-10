j, t, f = map(int, input().split())

judges = [tuple(map(int, input().split() + [i])) for i in range(j)]
tar = [tuple(map(int, input().split())) for _ in range(t)]
feathers = [tuple(map(int, input().split())) for _ in range(f)]

def distance(start, end):
    a = abs(start[0]-end[0])
    b = abs(start[1]-end[1])
    return (a**2+b**2)**0.5

tarLook = {}
for i in range(len(judges)):
    tarLook[i] = []
    for j in range(t):
        tarLook[i].append(distance(judges[i], tar[j]))


featherLook = {}
for i in range(len(judges)):
    featherLook[i] = []
    for j in range(f):
        featherLook[i].append(distance(judges[i], feathers[j]))
# print(featherLook)

dist = 0
judges2 = [i for i in judges]
while judges2:
    minDist = float('inf')
    minIndex = 0
    minIndT = 0
    for i in range(len(judges2)):
        if min(tarLook[judges2[i][-1]]) < minDist:
            minDist = min(tarLook[judges2[i][-1]])
            minIndex = i
            minIndT = tarLook[judges2[i][-1]].index(minDist)
    dist += minDist
    # print(judges2, minIndex)
    a = judges2.pop(minIndex)
    del tarLook[a[-1]]
    # print(tarLook, tarLook.keys())
    for i in tarLook.keys():
        tarLook[i].pop(minIndT)
# print(dist)

judges2 = [i for i in judges]
while judges2:
    minDist = float('inf')
    minIndex = 0
    minIndT = 0
    for i in range(len(judges2)):
        if min(featherLook[judges2[i][-1]]) < minDist:
            minDist = min(featherLook[judges2[i][-1]])
            minIndex = i
            minIndT = featherLook[judges2[i][-1]].index(minDist)
    dist += minDist
    a = judges2.pop(minIndex)
    del featherLook[a[-1]]
    for i in featherLook.keys():
        featherLook[i].pop(minIndT)

print(dist)