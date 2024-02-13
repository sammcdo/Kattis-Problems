import bisect
n = int(input())
array = [int(i) for i in input().split()]

sets = [[array[0]]]

for i in range(1, len(array)):
    pos = len(sets)
    x = 0
    y = len(sets)-1
    while x <= y:
        k = (x+y)//2
        if sets[k][-1] >= array[i]:
            x = k+1
        else:
            y = k-1
            pos=k
    # print(sets, array[i], k, pos)

    if pos == len(sets):
        sets.append([array[i]])
    elif sets[pos][-1] == array[i]:
        if pos+1 < len(sets):
            sets[pos+1].append(array[i])
        else:
            sets.append([array[i]])
    else:
        sets[pos].append(array[i])



print(len(sets))
for i in sets:
    print(*i)