h, k = map(int, input().split())

while not (h == 0 and k == 0):
    heads = [int(input()) for i in range(h)]
    knights = [int(input()) for i in range(k)]
    heads.sort()
    knights.sort()

    # print(heads)
    # print(knights)

    cost = 0
    while len(heads) > 0:
        current = heads.pop(0)

        foundKnight = False
        x = -1
        while len(knights) > 0:
            x = knights.pop(0)
            if x >= current:
                foundKnight = True
                break
        if not foundKnight:
            cost = -1
            break
        else:
            cost += x

    if cost == -1:
        print("Loowater is doomed!")
    else:
        print(cost)

    h, k = map(int, input().split())