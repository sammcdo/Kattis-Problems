import math
e, t = map(int, input().split())

entries = [int(input()) for _ in range(e)]

l, r = 0, 10**18

while l+1 < r:
    mid = l+(r-l)//2

    # min count 
    count = 0
    for i in range(e):
        count += (entries[i]-1)//mid+1
        # print(count, end=" ")
    # print()
    
    # print("\t", l, r, mid, count)
    if count <= t: # valid
        r = mid
    else: # not valid
        l = mid
    
print(r)