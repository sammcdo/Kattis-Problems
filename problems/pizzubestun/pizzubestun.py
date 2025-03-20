import heapq

n = int(input())

pizzas = []
heapq.heapify(pizzas)

for i in range(n):
    name, cost = input().split()
    cost = int(cost)
    
    heapq.heappush(pizzas, -cost)

# print(pizzas)

totalCost = 0
while len(pizzas) > 1:
    first = heapq.heappop(pizzas)
    second = heapq.heappop(pizzas)
    totalCost += -first
if len(pizzas) == 1:
    totalCost += -pizzas[0]

print(totalCost)