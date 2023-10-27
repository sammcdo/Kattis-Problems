b, d, c, l = map(int, input().split())

combos = []
found = False

for i in range(251):
    for j in range(251):
        for k in range(251):
            legs = i*b + j*d + k*c
            
            if legs == l:
                combos.append((i,j,k))
                found = True
            elif legs > l:
                break

if not found:
    print("impossible")
else:
    for i in sorted(combos):
        print(*i)