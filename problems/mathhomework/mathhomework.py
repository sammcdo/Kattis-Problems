a,b,c,target = map(int, input().split())

legs = [a,b,c]

sol = set()
i=j=k = 0
s = 0
while True:
    s = legs[0] * i
    while True:
        s += legs[1] * j
        
        while True:
            # print(i,j,k,s)
            s += legs[2] * k
            if s == target:
                sol.add((i,j,k))
            if s > target:
                s -= legs[2] * k
                k = 0
                break
            s -= legs[2] * k
            k += 1
        
        if s == target:
            sol.add((i,j,k))
        if s > target:
            s -= legs[1] * j
            j = 0
            break
        s -= legs[1] * j
        j += 1
    if s == target:
        sol.add((i,j,k))
    if s > target:
        break
    i += 1

sol = list(sol)
sol.sort()
if len(sol) > 0:
    for i in sol:
        print(*i)
else:
    print("impossible")