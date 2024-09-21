n = int(input())

h = list(map(int, input().split()))

l = 0
r = 1

if len(h) == 1:
    print(0)
    exit()

while r < len(h) and h[l] < h[r]:
    l+= 1
    r += 1

lowestMid = h[l]
m = 0
while r < len(h):
    lowestMid = min(lowestMid, h[r])

    if h[r] > lowestMid:
        m = max(m, min(h[l], h[r]) - lowestMid)
    
    if h[r] >= h[l]:
        l = r
        lowestMid = h[l]
    
    r+= 1
print(m)