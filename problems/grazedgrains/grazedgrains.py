import math
field = [[0]*1102 for i in range(1102)]

def interceptsAtI(i, coord, r):
    h,k = coord
    try:
        r = round(math.sqrt(abs(r**2 - (i-k)**2)) + h,4)
        l = -r#(math.sqrt(r**2 - (i-k)**2) + h)
    except:
        print("failed", h,k,i)

    return l,r

def circle(coord, r):
    x,y = coord
    x = 110 + (x*10)
    y = 110 + (y*10)

    for i in range(r*10):
        l,ri = interceptsAtI((i/10),(0,0),r)
        for j in range(0,round(ri*10)):
            field[y+i][x+j] = 1
            field[y+i][x-j] = 1
            field[y-i][x+j] = 1
            field[y-i][x-j] = 1

for i in range(int(input())):
    x,y,r = map(int, input().split())
    circle((x,y),r)

area = 0
for r in field:
    for i in r:
        area += 0.1 * i
    # print(sum(r), end=" ")

print(area/10)