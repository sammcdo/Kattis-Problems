# input
n, k, c = map(int, input().split())
ranks = []
for i in range(n):
    t, s = map(int, input().split())
    ranks.append([t, s])
order = []
orderSet = set()
filled = {}

# pass 1
i = 0
for t, s in ranks:
    if s in filled:
        if filled[s] >= c:
            i += 1
            continue
        else:
            filled[s] += 1
            order.append((i, t))
            orderSet.add(t)
    else:
        filled[s] = 1
        order.append((i, t))
        orderSet.add(t)
    i += 1

# pass 2
i = 0
for t, s in ranks:
    if t in orderSet:
        i += 1
        continue
    order.append((i, t))
    i += 1


# out
order = order[0:k]
order.sort()
for o in order:
    print(o[1])