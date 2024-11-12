n = int(input())

peaks = []
middle = -1
m = 0
for i in range(n):
    a,b = map(int, input().split())

    if b > m:
        middle = i
        m = b
    peaks.append((a,b))

def slope(mid, curr):
    y = abs(curr[1]-mid[1])
    x = abs(curr[0]-mid[0])
    return (y,x)

def cross(a,b):
    return (a[0]*b[1], a[1]*b[0])

l = middle
s = (10_000_000_000, 1)
for i in range(middle-1, -1, -1):
    thisS = slope(peaks[middle], peaks[i])
    a,b = cross(s, thisS)

    if a >= b:
        s = thisS
        if peaks[i][1] <= peaks[l][1]:
            l = i

r = middle
s = (10_000_000_000, 1)
for i in range(middle+1, n):
    thisS = slope(peaks[middle], peaks[i])
    a,b = cross(s, thisS)

    if a >= b:
        s = thisS
        if peaks[i][1] <= peaks[r][1]:
            r = i

print(*peaks[l])
print(*peaks[r])
