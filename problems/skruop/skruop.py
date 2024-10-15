n = int(input())

cmds = [input() for i in range(n)]

vol = 7

for i in cmds:
    if i == "Skru op!":
        vol += 1
        vol = min(vol, 10)
    else:
        vol -= 1
        vol = max(0,vol)

print(vol)