import math
from collections import deque

n = int(input())

gears = {}

output = 0

for i in range(n):
    s,c = map(int, input().split())
    if s not in gears:
        gears[s] = []
    gears[s].append(c)

for size, gearList in gears.items():
    gearList = deque(sorted(gearList))

    while len(gearList) > 1:
        smallest = gearList.popleft()
        largest = gearList.pop()
        output += math.log(largest / smallest)

print(output)