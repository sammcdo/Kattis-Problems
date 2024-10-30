from collections import deque

grid = [[int(i) for i in input().split()] for _ in range(3)]

moves = [
    [[0,0],[1,0],[2,0], [0,1],[0,2]],
    [[0,0],[1,0],[2,0], [1,1],[1,2]],
    [[0,0],[1,0],[2,0], [2,1],[2,2]],

    [[0,1],[1,1],[2,1], [0,0],[0,2]],
    [[0,1],[1,1],[2,1], [1,0],[1,2]],
    [[0,1],[1,1],[2,1], [2,0],[2,2]],

    [[0,2],[1,2],[2,2], [0,0],[0,1]],
    [[0,2],[1,2],[2,2], [1,0],[1,1]],
    [[0,2],[1,2],[2,2], [2,0],[2,1]],
]

def isValid(thing):
    for i in range(3):
        for j in range(3):
            if thing[i][j] != 0:
                return False
    return True

def applyMove(thing, move):
    for m in move:
        thing[m[1]][m[0]] += 1
        if thing[m[1]][m[0]] > 3:
            thing[m[1]][m[0]] = 0
    return thing

q = deque([(grid,0)])

visited = set()

while q:
    first, depth = q.popleft()
    # print(first, depth)
    
    if isValid(first):
        print(depth)
        exit(0)
    
    for move in moves:
        next = [[first[j][i] for i in range(3)] for j in range(3)]
        next = applyMove(next, move)
        # print("f", first)
        t = tuple(tuple(i) for i in next)
        # print("t", t)
        if t not in visited:
            visited.add(t)
            q.append((next, depth+1))
print(-1)