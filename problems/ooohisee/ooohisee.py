r, c = map(int, input().split())

grid = [input() for _ in range(r)]

found = []
for i in range(1, r-1):
    for j in range(1,c-1):
        if grid[i][j] == '0':
            works = True
            for x in range(-1,2):
                for y in range(-1,2):
                    if x == 0 and y == 0:
                        continue
                    if grid[i+x][j+y] != 'O':
                        works=False
                        break
                if not works:
                    break
            if works:
                found.append((i+1,j+1))

if len(found) == 0:
    print("Oh no!")
elif len(found) == 1:
    print(*found[0])
else:
    print(f'Oh no! {len(found)} locations')
