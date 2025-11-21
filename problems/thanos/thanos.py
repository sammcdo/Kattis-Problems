import math
for _ in range(int(input())):
    p,r,f = map(int, input().split())

    c = 0
    while p <= f:
        c += 1
        p = p*r

    print(c)