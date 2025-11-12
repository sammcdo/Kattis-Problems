a = input().split()

while a!= ["0.0", "0"]:
    r = float(a[0])
    r2 = r * r
    n = int(a[1])

    pts = []
    sour = [0] * n
    for i in range(n):
        x, y = map(float, input().split())
        pts.append([x,y])


    for x in range(n-1):
        for y in range(x+1, n):
            if (pts[x][0]-pts[y][0])**2 + (pts[x][1]-pts[y][1])**2 <= r2:
                sour[x] = 1
                sour[y] = 1
    
    count = sum(sour)
    
    print(str(count) + " sour, " + str(n-count) + " sweet")

    a = input().split()