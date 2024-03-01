n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

results = []
for k in range(2, 51):
    if n % k != 0:
        continue

    mins, maxes = [], []
    size_of_section = n // k
    for i in range(0, n, size_of_section):
        arr = l[i:i + size_of_section]
        maxes.append(max(arr))
        mins.append(min(arr))
    valid = True
    for i in range(k):
        if i > 0:
            if maxes[i - 1] > mins[i]:
                valid = False
                break
    if not valid:
        continue
    results.append(k)

if not results:
    print(-1)
else:
    results.sort()
    for v in results:
        print(v)