_, white = input().split(":")
_, black = input().split(":")
white = white.split(",")
black = black.split(",")
sides = [white, black]

board = []
for i in range(8):
    a = []
    for j in range(8):
        a.append(list(":::" if i%2 == j%2 else "..."))
    board.append(a)


for side in sides:
    for piece in side:
        piece = piece.strip()
        if piece == "":continue
        y = int(piece[-1]) - 1
        x = ord(piece[-2]) - ord('a')
        type_ = piece[:-2]
        if type_ == "":
            type_ = "p"
        if side != white:
            type_ = type_.lower()
        else:
            type_ = type_.upper()

        board[y][x][1] = type_

def rowDecor():
    print("+---" * 8 + "+")

rowDecor()
for row in reversed(board):
    print("|",end="")
    for cell in row:
        print("".join(cell) + "|",end="")
    print()
    rowDecor()