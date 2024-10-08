n, k = map(int, input().split())

times = []

for i in range(n):
    start, end = map(int, input().split())

    times.append((start,0))
    times.append((end,1))

left, right = 0, 0

times.sort()
# print(times)

inRange = 0
final = 0
while left < len(times):
    start = times[left][0]
    while right < len(times) and times[right][0] - start <= k:
        end = times[right]
        right += 1
        if end[1] == 1:
            pass
        else:
            inRange += 1
    # print(left, right, inRange)
    final = max(inRange, final)
    if times[left][1] == 1:
        inRange -= 1
    left += 1

print(final)
