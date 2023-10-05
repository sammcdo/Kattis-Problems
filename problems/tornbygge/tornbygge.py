input()

bricks = map(int, input().split())
towers = 0
prev = 0

for b in bricks:
    if b > prev:
        towers += 1
    prev = b

print(towers)
