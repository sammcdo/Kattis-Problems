def triangle(n):
    return (n+1)*n // 2

n, k = map(int, input().split())

gaps = []
for i in range(k):
    gaps.append(int(input()))

total = triangle(n)
lastGap = 0
gaps.append(n+1)
for gap in gaps:
    diff = gap - lastGap
    total -= triangle(diff-1)
    lastGap = gap


print(total)