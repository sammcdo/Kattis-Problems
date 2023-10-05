test = input()

pos = [1,0,0]

for l in test:
    if l == "A":
        a = pos[0]
        b = pos[1]
        pos[0] = b
        pos[1] = a
    elif l == "B":
        a = pos[1]
        b = pos[2]
        pos[1] = b
        pos[2] = a
    else:
        a = pos[0]
        b = pos[2]
        pos[0] = b
        pos[2] = a

print(pos.index(1)+1)
