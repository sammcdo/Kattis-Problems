import sys

n = int(input())

cost = int(input())

avg = int(input())

places = [int(i) for i in input().split()]

places.sort()

sum = 0
for i in range(1, len(places)+1):
    x = places[i-1]

    sum += x * cost
    if sum*1.0/i > avg:
        print(i-1)
        sys.exit()

print(len(places))