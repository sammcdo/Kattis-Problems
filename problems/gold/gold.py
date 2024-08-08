w, h = map(int, input().split())

plan = []

pos = (0, 0)
for i in range(h):
    row = input()

    x = row.find("P")
    if x != -1:
        pos = (i, x)
    
    plan.append(row)


def walk(start):
    stack = []
    visited = {}
    gold = 0

    stack.append(start)

    while stack:
        pos = stack.pop()

        if pos not in visited:
            visited[pos] = True
        else:
            continue

        if plan[pos[0]][pos[1]] == "G":
            gold += 1
        
        if plan[pos[0]][pos[1]] == "#":
            continue
        
        opts = [
            (1,0),(0,1),(-1,0),(0,-1)
        ]

        next = []
        for op in opts:
            a = pos[0] + op[0]
            b = pos[1] + op[1]

            if a >= 0 and b >= 0 and a < h and b < w:
                if plan[a][b] != "T":
                    next.append((a,b))
        
        if len(next) == 4:
            stack.extend(next)
    
    return gold

gold = walk(pos)

print(gold)