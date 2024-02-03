def toBase(num, base):
    places = []
    if num == 0:
        places.append(0)
        return places
    while num:
        places.append(num % base)
        num = num // base
    return places

def isPal(places):
    p1 = 0
    p2 = len(places)-1
    half = len(places) // 2

    for i in range(0, half+1):
        if places[p1] != places[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True

x, y, b = map(int, input().split())

works = [i for i in range(x, y+1)]
works2 = []
for j in range(2, b+1):
    for i in works:
        n = toBase(i, j)
        if isPal(n):
            works2.append(i)
    works = works2
    works2 = []

print(len(works))

