import math
import sys
sys.setrecursionlimit(10**9)

INF = 10**18

def build(n):
    size = 1
    while size < n: size *= 2
    seg = [INF] * (2 * size)
    return seg, size

def update(seg, size, pos, val):
    pos += size
    seg[pos] = min(seg[pos], val)
    pos //= 2
    while pos:
        seg[pos] = min(seg[2*pos], seg[2*pos+1])
        pos //= 2

def query(seg, size, l, r):
    if l > r: 
        return INF
    l += size
    r += size
    res = INF
    while l <= r:
        if l & 1:
            res = min(res, seg[l])
            l += 1
        if not (r & 1):
            res = min(res, seg[r])
            r -= 1
        l //= 2
        r //= 2
    return res

    
def do():
    n = int(input())
    workers = [tuple(int(i) for i in input().split()) for _ in range(n)]
    workers.sort()#key=lambda x: -min(x))

    seg, size = build(n+1)

    proc = n
    works = 0

    for a, b, c in workers:
        # check if any worker with b' < b has c' < c
        minimum = query(seg, size, 1, b-1)
        if minimum < c:
            # dominated
            continue
        works += 1
        update(seg, size, b, c)
    
    print(works)
    # print(tree)
    # print("\n\n")



tc = int(input())
for i in range(tc):
    do()