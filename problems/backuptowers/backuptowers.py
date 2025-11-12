from collections import deque

def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

R,C,n = map(int, input().split())

spots = [[int(i)-1 for i in input().split()] for _ in range(n)]

grid1 = [[[(float('inf'), None), (float('inf'), None)] for c in range(C)] for _ in range(R)]

q = deque()
for i in range(n):
    tr, tc = spots[i]
    grid1[tr][tc][0] = (0,i+1)
    q.append((tr,tc,i+1,0))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
while q:
    r,c,src,d = q.popleft()
    # print(r,c,src,d)

    if grid1[r][c][0][1] == src and grid1[r][c][0][0] < d:
        continue

    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if not (0 <= nr < R and 0 <= nc < C): continue
        nd = d+1
    
        entries = grid1[nr][nc]
        updated = False
        for i in [0,1]:
            if entries[i][1] == src:
                if nd < entries[i][0]:
                    entries[i] = (nd, src)
                    updated = True
                break
        else:
            # src not present yet
            if nd < entries[1][0]:
                entries[1] = (nd, src)
                updated = True
        if updated:
            # sort entries by distance
            if entries[1][0] < entries[0][0]:
                entries[0], entries[1] = entries[1], entries[0]
            # enqueue neighbor
            q.append((nr, nc, src, nd))
    

for r in grid1:
    for c in r:
        print(c[0][1], end=" ")
    print()
# print()
for r in grid1:
    for c in r:
        print(c[1][1], end=" ")
    print()