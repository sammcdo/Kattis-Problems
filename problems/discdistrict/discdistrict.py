import math

def dist(x,y):
    return math.sqrt(x**2+y**2)

r = int(input())

closest = float('inf')
coords = (-1,-1)
x = r+1
for y in range(r+1):
    while dist(x,y) > r:
        x -= 1
    x += 1
    d = dist(x,y)
    # print(x,y,d)
    if d < closest:
        closest = d
        coords = (x,y)

print(*coords)