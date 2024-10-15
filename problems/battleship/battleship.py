n = int(input())

for x in range(n):
    w,h, turns = map(int, input().split())

    mapA = []
    boatsA = set()
    mapB = []
    boatsB = set()
    for i in range(h):
        mapA.append(list(input()))
        for j in range(w):
            if mapA[i][j] == "#":
                boatsA.add((j, h-i-1))
    
    for i in range(h):
        mapB.append(list(input()))
        for j in range(w):
            if mapB[i][j] == "#":
                boatsB.add((j, h-i-1))
    shots = [tuple([int(i) for i in input().split()]) for _ in range(turns)]
    # print(shots)
    # print(boatsA)
    # print(boatsB)

    i = 0
    while True:
        # print(boatsA)
        # print(boatsB)
        # person A turn
        while True:
            if i >= turns:
                break
            a = shots[i]
            i += 1
            if a in boatsB:
                # print(boatsB, end=" : ")
                boatsB.remove(a)
                # print(boatsB)
                if len(boatsB) == 0:
                    break
            else:
                break
        # person B turn
        while True:
            if i >= turns:
                break
            a = shots[i]
            i += 1
            if a in boatsA:
                # print(boatsA, end=" : ")
                boatsA.remove(a)
                # print(boatsA)
                if len(boatsA) == 0:
                    break
            else:
                break
        
        if len(boatsA) == 0 and len(boatsB) == 0:
            print("draw")
            break
        elif len(boatsA) == 0:
            print("player two wins")
            break
        elif len(boatsB) == 0:
            print("player one wins")
            break
        elif i >= turns:
            print("draw")
            break

