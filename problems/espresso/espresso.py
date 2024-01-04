import math

n, s = map(int, input().split())

total = s
fills = 0
for i in range(n):
    x = input()
    count = 0
    if x.endswith("L"):
        x = x.replace("L", "")
        count += 1
    x = int(x)
    count += x
    if count > total:
        total = s
        total -= count
        fills += 1
    else:
        total -= count

print(fills)
