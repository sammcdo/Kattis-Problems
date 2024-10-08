n = int(input())
bar = 2*n

counts = {}

for i in range(10*n):
    row = list(map(int, input().split()))
    for num in row:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1

works = []
for i,v in counts.items():
    if v > bar:
        works.append(i)

if len(works) > 0:
    print(*sorted(works))
else:
    print(-1)