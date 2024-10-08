from math import dist

x1,y1, x2,y2, a = map(int, input().split())

def inbounds(x,y):
    b = dist((x,y), (x1,y1))
    c = dist((x,y), (x2,y2))
    if b+c <= a:
        return True
    return False

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
closest = [
    (x1,y1) if x1 > x2 else (x2,y2),
    (x1,y1) if y1 > y2 else (x2,y2),
    (x1,y1) if x1 < x2 else (x2,y2),
    (x1,y1) if y1 < y2 else (x2,y2),
]

dims = []
for i in range(len(dirs)):
    xdir, ydir = dirs[i]
    cx,cy = closest[i]
    step = 1

    while step > 10**-6:
        while 1:
            tx = cx + xdir * step
            ty = cy + ydir * step
            if inbounds(tx, ty):
                cx = tx
                cy = ty
            else:
                break
        if ydir != 0:
            nx = cx
            nx2 = cx
            while inbounds(nx-step,cy):
                nx -= step
            while inbounds(nx2+step, cy):
                nx2 += step
            cx = (nx+nx2) / 2
        else:
            ny = cy
            ny2 = cy
            while inbounds(cx,ny-step):
                ny -= step
            while inbounds(cx, ny2+step):
                ny2 += step
            cy = (ny+ny2) / 2
        step /= 2
    if ydir != 0:
        dims.append(cy)
    else:
        dims.append(cx)

print(dims[2],dims[3], dims[0],dims[1])