import bisect

pals = []

for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            i, j, k = str(i), str(j), str(k)
            pals.append(i+j+k+k+j+i)

pals.sort()

for i in range(int(input())):
    this = input()
    x = bisect.bisect_right(pals, this)
    a,b = pals[x-1], pals[x]
    # print(a,b)

    if abs(int(a)-int(this)) <= abs(int(b)-int(this)):
        print(a)
    else:
        print(b)

# print(pals)