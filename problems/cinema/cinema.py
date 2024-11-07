n, m = map(int, input().split())
groups = [int(i) for i in input().split()]
counted = 0

for i in range(m):
    n -= groups[i]
    if n < 0:
        n += groups[i]
        continue
    counted += 1

print(m-counted)