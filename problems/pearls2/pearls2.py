la, lb, k, q = map(int, input().split())

a = input()
b = input()

bad = set()

for i in range(k):
    x,y = input().split()
    bad.add((x,y))

queries = [int(input()) for i in range(q)]

lookup = {i:[False] for i in "abcdefghijklmnopqrstuvwxyz"}

necklace = []

qLookup = {i:0 for i in queries}
qSorted = list(sorted(queries))

ind = 0
sind = 0
for x in a:
    # print(x)
    if lookup[x] == [False]:
        lookup[x] = []
        for y in b:
            if (x,y) not in bad:
                lookup[x].append(x)
                lookup[x].append(y)
    oldInd = ind
    ind += len(lookup[x])
    while sind < len(qSorted) and qSorted[sind] < ind:
        qLookup[qSorted[sind]] = lookup[x][qSorted[sind]-oldInd]
        sind += 1

# print(necklace)
for i in queries:
    print(qLookup[i])