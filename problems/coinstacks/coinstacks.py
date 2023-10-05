count = int(input())

stacks = [int(i) for i in input().split()]
total = sum(stacks)

solvable = True
moves = []

while total > 0:
    m1 = [0, -1]
    m2 = [1001, -1]
    for i in range(len(stacks)):
        if stacks[i] == 0:
            continue
        elif stacks[i] >= m1[0]:
            prev = m1.copy()
            m1[0] = stacks[i]
            m1[1] = i

            if prev[0] <= m2[0] and prev != [0, -1]:
                m2[0] = prev[0]
                m2[1] = prev[1]

        elif stacks[i] <= m2[0]:
            m2[0] = stacks[i]
            m2[1] = i

    if m1[1] == -1 or m2[1] == -1:
        if total != 0:
            solvable = False
            break
    moves.append(str(m1[1]+1)+" "+str(m2[1]+1))
    stacks[m1[1]] = stacks[m1[1]] - 1
    stacks[m2[1]] = stacks[m2[1]] - 1
    total -= 2

if solvable:
    print("yes")
    for i in moves:
        print(i)
else:
    print("no")