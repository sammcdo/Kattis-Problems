r, c = map(int, input().split())

grid = [input() for i in range(r)]

visited = set()
curr = [0,0]
count = 0
while True:
    # print(curr)
    visited.add(tuple(curr))

    dir = grid[curr[0]][curr[1]]

    if dir == "N":
        curr[0] -= 1
    elif dir == "S":
        curr[0] += 1
    elif dir == "E":
        curr[1] += 1
    elif dir == "W":
        curr[1] -= 1
    else:
        print(count)
        break
    
    count +=  1

    if curr[0] < 0 or curr[0] >= r or curr[1] < 0 or curr[1] >= c:
        print("Out")
        break

    if tuple(curr) in visited:
        print("Lost")
        break

