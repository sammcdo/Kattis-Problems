import bisect
n = int(input())

sticks = [int(i) for i in input().split()]

sticks.sort()
# print(sticks)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        mins = abs(sticks[i]-sticks[j])
        maxs = sticks[i] + sticks[j]
        l = bisect.bisect_right(sticks, mins)
        r = bisect.bisect_left(sticks,maxs)
        # print(mins, maxs, l, r)
        if r-l > 2:
            print("possible")
            exit()
print("impossible")

