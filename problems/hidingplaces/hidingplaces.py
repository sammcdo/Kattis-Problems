import math

ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))


def algToXY(a):
  x, y = list(a)
  return 'abcdefgh'.index(x), int(y)-1
def xyToAlg(x, y):
  xx = 'abcdefgh'[x]
  return f'{xx}{y+1}'
dirs = (
  (-2, 1),
  (2, 1),
  (-1, 2),
  (1, 2),


  (-2, -1),
  (2, -1),
  (-1, -2),
  (1, -2),
)

n = ii()
for _ in range(n):
  x, y = algToXY(input())

  grid = []
  for _ in range(8):
    grid.append([-1] * 8)
  grid[y][x] = 0
  
  jumps = 1
  hasJump = 1
  while hasJump:
    hasJump = 0
    for y in range(8):
      for x in range(8):
        if grid[y][x] == jumps-1:
          for dx, dy in dirs:
            xx = x + dx
            yy = y + dy
            if xx < 0 or xx >= 8 or yy < 0 or yy >= 8:
              continue
            if grid[yy][xx] == -1:
              grid[yy][xx] = jumps
              hasJump = 1
    jumps += 1

  li = []
  mostJumps = jumps - 2
  for y in range(8):
    for x in range(8):
      if grid[y][x] == mostJumps:
        li.append((x,y))

  li.sort(key=lambda x: (x[1],-x[0]), reverse=True)
  li = [xyToAlg(*i) for i in li]

  print(mostJumps, *li)