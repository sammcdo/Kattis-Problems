def toStr(x, l):
    x = str(x)
    if len(x) < l:
        x = "0"*(l-len(x))+x
    return x

k, n = map(int, input().split())

works = []

codes = [input() for i in range(n)]

# brute force test all possible codes
for i in range(10**k):
    test = toStr(i, k)
    working = True

    for code in codes:
        j = 0
        for x in range(len(code)):
            if code[x] == test[j]:
                j += 1
                if j == k:
                    break
        if j < k:
            working = False
            break
    
    if working:
        works.append(test)

print(len(works))
for w in works:
    print(w)