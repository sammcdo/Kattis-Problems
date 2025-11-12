parked = [0]*101

a,b,c = map(int, input().split())

for i in range(3):
    x,y = map(int, input().split())
    for j in range(x,y):
        parked[j] += 1

cost = 0
for i in parked:
    if i == 0:
        continue
    if i == 1:
        cost += a
    if i == 2:
        cost += b+b
    if i == 3:
        cost += c*3

print(cost)