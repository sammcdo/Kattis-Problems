n = int(input())

seq = [int(input()) for _ in range(n)]

i = 0
cost = 0
while i < n-1:
    cost += max(seq[i:i+2])
    i += 1

print(cost)