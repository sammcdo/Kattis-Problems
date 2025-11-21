import functools
import sys

n = int(input())

letters = [i for i in range(1,n+1)]

lookup = {}
def query(letters):
    global lookup
    x = tuple(letters)
    if x in lookup:
        return lookup[x]
    # print(lookup)
    print(*letters, flush=True)
    a = int(input())
    if a == n:
        sys.exit()
    lookup[x] = a
    return a

correct = query(letters)
final = set()
for i in range(n):
    if i in final:
        continue
    init = correct
    found = False
    temp = []
    for j in range(i+1, n):
        # print("swapping", i, j)
        if j in final:
            continue
        letters[i], letters[j] = letters[j], letters[i]
        correct = query(letters)
        if correct == init + 2:
            final.add(i)
            final.add(j)
            found = True
            break
        elif correct == init + 1:
            temp.append(j)
            letters[i], letters[j] = letters[j], letters[i]
        else:
            letters[i], letters[j] = letters[j], letters[i]
    if len(temp) == 2 and not found:
        a,b,c = i, temp[0], temp[1]

        XX = letters[:]
        letters[a], letters[b] = letters[b], letters[a]
        letters[b], letters[c] = letters[c], letters[b]
        c1 = query(letters)
        #undo
        letters = XX[:]
        letters[a], letters[c] = letters[c], letters[a]
        letters[b], letters[c] = letters[c], letters[b]
        c2 = query(letters)
        if c1 < c2:
            found = True
            correct = c2
        else:
            letters = XX[:]
            letters[a], letters[b] = letters[b], letters[a]
            letters[b], letters[c] = letters[c], letters[b]
            found = True
            correct = c1
        if c1 == init+3 or c2 == init+3:
            final.add(b)
            final.add(c)
        final.add(a)
        found = True
    if not found:
        final.add(i)
    correct = query(letters)
query(letters)