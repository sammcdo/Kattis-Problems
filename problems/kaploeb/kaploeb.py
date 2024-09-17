import heapq

l, k, s = map(int, input().split())

people = {}

finished = []
heapq.heapify(finished)

for i in range(l):
    name, time = input().split()
    name = int(name)
    mins, sec = map(int, time.split("."))
    sec += 60*mins

    if name not in people:
        people[name] = [0,0]
    
    if people[name][1] < k:
        people[name][0] += sec
        people[name][1] += 1
        if people[name][1] == k:
            x = [people[name][0], name]
            heapq.heappush(finished, x)


for i in range(len(finished)):
    print(heapq.heappop(finished)[1])