n = int(input())

def dist(first, second):
    y = abs(first[1] - second[1])
    x = abs(first[0] - second[0])
    return (x**2+y**2)**0.5

for i in range(n):
    size, h = map(int, input().split())
    hatches = []

    for i in range(h):
        x,y = map(int, input().split())
        hatches.append((x,y))
    
    hatchLook = set(hatches)

    possible = (float('inf'), float('inf'))
    
    for i in range(1,size-1):
        for j in range(1, size-1):
            coords = (i,j)
            maxDist = min(i, size-i, j, size-j)

            if coords in hatchLook:
                continue

            found = True
            for x in hatches:
                if dist(coords, x) > maxDist:
                    found = False
            if found:
                possible = min(possible, coords)
    
    if possible == (float('inf'), float('inf')):
        print("poodle")
    else:
        print(*possible)
