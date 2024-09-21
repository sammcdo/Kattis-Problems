board = [input() for i in range(3)]

combos = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],

    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],

    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)],
]

hasGood = False
hasBad = False
for s in combos:
    a,b,c = s
    if board[a[0]][a[1]] == "O" and board[b[0]][b[1]] == "O" and board[c[0]][c[1]] == "O":
        hasGood = True
    elif board[a[0]][a[1]] == "X" and board[b[0]][b[1]] == "X" and board[c[0]][c[1]] == "X":
        hasBad = True

if hasBad:
    print("Neibb")
elif hasGood:
    print("Jebb")
else:
    print("Neibb")