n = int(input())

dirs = [(1,0), (0,1), (-1,0), (0,-1)]

grid = []
for i in range(n):
    row = input()
    grid.append(list(row))

for i in range(n):
    for j in range(n):
        if grid[i][j] == "?":
            for d in dirs:
                x,y = i,j
                while x >=0 and x < n and y >=0 and y < n:
                    x,y = x+d[0], y+d[1]
                    if x >=0 and x < n and y >=0 and y < n:
                        if grid[x][y] == "X" or grid[x][y].isdigit():
                            break
                        elif grid[x][y] == "?":
                            # print(i,j,x,y, "q")
                            print(0)
                            exit()
                        else:
                            grid[x][y] = "*"

# for i in grid:
#     print(i)

for i in range(n):
    for j in range(n):
        if grid[i][j] == ".":
            print(0)
            exit()
        if grid[i][j].isdigit():
            c = 0
            for d in dirs:
                x,y = i+d[0], j+d[1]
                if x >= 0 and x < n and y >= 0 and y < n:
                    if grid[x][y] == "?":
                        c += 1
            if c != int(grid[i][j]):
                print(0)
                exit()

print(1)