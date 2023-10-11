import heapq
a, b = map(int, input().split())

nums = {}
for i in range(1,a+1):
    for j in range(1,b+1):
        if i+j in nums:
            nums[i+j] += 1
        else:
            nums[i+j] = 1

data = [[-v, k] for k, v in nums.items()]

heapq.heapify(data)

prev = data[0][0]
while data[0][0] == prev:
    print(heapq.heappop(data)[1])