n, lph = map(int, input().split())

probs = [int(input()) for _ in range(n)]
probs.append(25001)
probs.sort()

total = 5 * lph
count = 0

while total >= 0:
    total -= probs.pop(0)
    count += 1

count -= 1

print(max(count, 0))