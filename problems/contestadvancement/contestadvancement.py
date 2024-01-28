import heapq

n, k, c = map(int, input().split())

schools = {}

items = []

output = []
remaining = []

for i in range(n):
    id, school = map(int, input().split())

    if school not in schools:
        schools[school] = []

    if len(schools[school]) < c:
        schools[school].append(id)
        output.append([i, id])
    else:
        heapq.heappush(remaining, [i, id])

    if len(output) == k:
        break

while len(output) < k:
    output.append(heapq.heappop(remaining))

output.sort()

for i in output:
    print(i[1])