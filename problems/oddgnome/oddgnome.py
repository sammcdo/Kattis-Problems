n = int(input())

for i in range(n):
    l = list(map(int, input().split()[1:]))
    mi = l[0]
    ma = l[-1]

    last = -1
    for i, v in enumerate(l):
        if i == 0:
            continue
        else:
            if l[i-1] + 1 != l[i]:
                print(i+1)
                break
        last = v