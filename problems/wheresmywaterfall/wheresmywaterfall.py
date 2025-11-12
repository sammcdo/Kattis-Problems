from collections import deque

n, m, k = map(int, input().split())

waterfalls = [int(i) for i in input().split()]

mario = [list(input()) for i in range(n)]

q = deque()

for i in waterfalls:
    q.append((i,0))

visited = set()
while q:
    loc = q.popleft()
    # print(loc)
    if loc in visited:
        continue
    visited.add(loc)
    mario[loc[1]][loc[0]] = "~"

    

    if loc[1] == n-1:
        continue
    
    if mario[loc[1]+1][loc[0]] in "#?":
        if loc[0] > 0 and mario[loc[1]][loc[0]-1] not in "#?~" and (loc[0]-1,loc[1]) not in visited:
            q.append((loc[0]-1,loc[1]))
        if loc[0] < m-1 and mario[loc[1]][loc[0]+1] not in "#?~" and (loc[0]+1,loc[1]) not in visited:
            q.append((loc[0]+1,loc[1]))
    else:
        if (loc[0],loc[1]+1) not in visited:
            q.append((loc[0],loc[1]+1))

for i in mario:
    print("".join(i))