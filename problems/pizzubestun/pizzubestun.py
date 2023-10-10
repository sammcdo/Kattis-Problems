import heapq

heap = []

for i in range(int(input())):
    x = int(input().split()[1])
    heapq.heappush(heap, -x)

sum = 0
while len(heap) > 1:
    sum += heapq.heappop(heap)
    heapq.heappop(heap)
if len(heap) == 1:
    sum += heapq.heappop(heap)

print(-sum)