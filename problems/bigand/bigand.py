import heapq

n, d, l = map(int, input().split())

h = [int(i) for i in input().split()]

heapq.heapify(h)

# put them in a heap so it is sorted min first
# if a switch has lower time to flip it should
# have more and gates
while len(h) >= 2:
    a = heapq.heappop(h)
    b = heapq.heappop(h)

    c = max(a,b) + d
    heapq.heappush(h,c)

# when there is only one input available 
# find final result
x = heapq.heappop(h)
print(x+l)
