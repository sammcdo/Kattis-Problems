import bisect

def lis(a, b):
    lookup = {}
    for i in range(len(a)):
        lookup[a[i]] = i
    
    b = [i for i in b if i in lookup]
    
    lis = [b[0]]

    for i in range(1, len(b)):
        this = lookup[b[i]]
        pos = bisect.bisect_right(lis, this)
        if pos == len(lis):
            lis.append(this)
        else:
            lis[pos] = this
        
        # print(this, lis)

    return len(lis)




n = int(input())

for i in range(n):
    size, x, y = map(int, input().split())

    xs = [int(i) for i in input().split()]
    ys = [int(i) for i in input().split()]




    print("Case "+str(i+1)+":", lis(xs, ys))
