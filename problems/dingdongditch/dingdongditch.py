n, m = map(int, input().split())

doors = [int(i) for i in input().split()]
counts = [int(i) for i in input().split()]
doors.sort()

sums = [0]

for i in range(0,n):
    sums.append(sums[-1]+doors[i])

for i in range(m):
    print(sums[counts[i]])