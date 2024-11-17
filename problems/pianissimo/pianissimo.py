import bisect
n, m = map(int, input().split())

notes = [int(input()) for i in range(n)]

d = ["ppp", "pp", "p", "mp", "mf", "f", "ff", "fff"]
lookup = {i:[] for i in d}

a_p, b_p = input().split()
a_p = int(a_p) - 1
for i in range(m-1):
    a,b = input().split()
    a = int(a)-1
    lookup[b_p].extend(notes[a_p:a])
    a_p = a
    b_p = b

lookup[b_p].extend(notes[a_p:])

for i in d:
    lookup[i].sort()

combos = 0
for first in range(len(d)):
    for sec in range(first+1, len(d)):
        x,y = d[first], d[sec]
        if len(lookup[x]) and len(lookup[y]) and lookup[x][-1] >= lookup[y][0]:
            e = bisect.bisect_left(lookup[x], lookup[y][0])
            s = bisect.bisect_right(lookup[y], lookup[x][-1])-1
            f = len(lookup[x])-1
            # print(lookup[x])
            # print(lookup[y])
            while s >= 0 and f >= e:
                # print(f, s)
                if lookup[x][f] >= lookup[y][s]:
                    combos += s+1
                f -= 1
                if f < e:
                    break
                while s >= 0 and lookup[x][f] < lookup[y][s]:
                    s -= 1
                

print(combos)