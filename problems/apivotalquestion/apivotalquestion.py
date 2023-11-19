array = [int(i) for i in input().split()]

l = array.pop(0)

works = []

maxAt = [0]*len(array)
minAt = [0]*len(array)

c_m = 0
for i in range(len(array)):
    if array[i] > c_m:
        c_m = array[i]
    maxAt[i] = c_m

c_m = 10**6 +1
for i in range(len(array)-1, -1, -1):
    if array[i] < c_m:
        c_m = array[i]
    minAt[i] = c_m

for i in range(len(array)):
    if maxAt[i] <= array[i] and minAt[i] >= array[i]:
        works.append(array[i])


if len(works) > 0:
    l = len(works)
    if len(works) > 100:
        works = works[0:100]
    print(l, *works)
else:
    print(0)