import sys

def makeSuffixArray(string):
    string = [ord(string[i]) for i in range(len(string))]
    string.append(30)
    n = len(string)
    alpha = 300
    p = [0 for i in range(n)]
    pn = [0 for i in range(n)]
    c = [0 for i in range(n)]
    cn = [0 for i in range(n)]
    cnt = [0 for i in range(max(alpha, n))]

    for i in range(n):
        cnt[string[i]] += 1
    for i in range(1, alpha):
        cnt[i] += cnt[i-1]
    for i in range(n):
        cnt[string[i]] -= 1
        x = cnt[string[i]]
        p[x] = i
    
    c[p[0]] = 0
    classes = 1
    for i in range(1, n):
        if string[p[i]] != string[p[i-1]]:
            classes += 1
        c[p[i]] = classes - 1

    for h in range(100000):
        if 1 << h >= n:
            break

        for i in range(n):
            pn[i] = p[i] - (1<<h)
            if pn[i] < 0:
                pn[i] += n
        
        for i in range(classes):
            cnt[i] = 0

        for i in range(n):
            cnt[c[pn[i]]] += 1
        
        for i in range(1, classes):
            cnt[i] += cnt[i-1]
        
        for i in range(n-1, -1, -1):
            cnt[c[pn[i]]] -= 1
            x = cnt[c[pn[i]]]
            p[x] = pn[i]
        
        cn[p[0]] = 0
        classes = 1
        for i in range(1, n):
            curr = (c[p[i]], c[(p[i] + (1<<h)) % n])
            prev = (c[p[i-1]], c[(p[i-1] + (1<<h)) % n])
            if curr != prev:
                classes += 1
            cn[p[i]] = classes - 1
        
        c, cn = cn, c
    return p

while True:
    try:
        word = input().strip()
        queries = list(map(int, input().split()))[1::]

        p = makeSuffixArray(word)

        for i in queries:
            print(p[i+1], end=" ")
        print()
    except:
        break
