q = []
foundi = []
foundj = []

for i in range(8):
    row = input()
    for j in range(8):
        if row[j] == "*":
            if i in foundi:
                print("invalid")
                quit()
            else:
                foundi.append(i)
            if j in foundj:
                print("invalid")
                quit()
            else:
                foundj.append(j)
            q.append([i, j])

if len(q) != 8:
    print("invalid")
    quit()

for x in range(7):
    for y in range(x+1, 8):
        if abs(q[x][0]-q[y][0]) == abs(q[x][1]-q[y][1]):
            print("invalid")
            quit()


print("valid")