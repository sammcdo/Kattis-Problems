a, b = [int(i) for i in input().split()]

locs = [int(i) for i in input().split()]

for i in range(b):
    x, y, z = [int(i) for i in input().split()]
    
    if x == 1:
        locs[y-1] = z
    else:
        dist = max(locs[y-1] - locs[z-1], locs[z-1] - locs[y-1])
        print(dist)