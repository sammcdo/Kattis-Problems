costA, capA, costB, capB, n = map(int, input().split())

m = float('inf')
t = (n // capA) + 1
x = [0, 0]

for i in range(t):
    tripsA = i
    totA = tripsA * costA
    takenA = tripsA * capA
    tripsB = (n - takenA) // capB
    if (n - takenA) % capB:
        tripsB += 1
    totB = tripsB * costB
    takenB = tripsB * capB

    if totA + totB < m:
        x = [tripsA, tripsB]
        m = totA + totB

print(*x, m)