n = int(input())
animals = [int(input()) for _ in range(n)]

animals.sort(reverse=True)

attackers = animals[0]
aCount = 1
defenders = 0
dCount = 0

for i in animals[1::]:
    defenders += i
    dCount += 1
    if defenders >= attackers:
        attackers += defenders
        aCount += dCount
        dCount = 0
        defenders = 0

print(aCount)