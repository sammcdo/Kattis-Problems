n = int(input())


grid = []
for i in range(n):
    grid.append(input())


for i in range(n):
    seq = ""
    b = 0
    for j in range(n):
        seq += grid[i][j]
        if grid[i][j] == 'B':
            b += 1
    if 'BBB' in seq or b != n // 2:
        print(0)
        quit()

for i in range(n):
    seq = ""
    b = 0
    for j in range(n):
        seq += grid[j][i]
        if grid[j][i] == 'B':
            b += 1
    if 'BBB' in seq or b != n // 2:
        print(0)
        quit()

print(1)