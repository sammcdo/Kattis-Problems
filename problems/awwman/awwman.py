t = int(input())

for i in range(t):
    daylen, unsafe = map(int, input().split())

    a,b,d = map(int, input().split())

    tripTime = b-a
    
    badTime = daylen - unsafe

    tot = b + tripTime + d
    if tot % (daylen+1) > badTime:
        print("NO")
    else:
        print("YES")