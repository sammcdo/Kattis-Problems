def checkHorizontal(board):
    out = []
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        out.append(board[0][0])
    if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        out.append(board[1][0])
    if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        out.append(board[2][0])
    return out

def checkVertical(board):
    out = []
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        out.append(board[0][0])
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        out.append(board[0][1])
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        out.append(board[0][2])
    return out

def checkDiagonal(board):
    out = []
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        out.append(board[0][0])
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        out.append(board[0][2])
    return out

board = []

for i in range(3):
    board.append(input().split())

found = []
found.extend(checkHorizontal(board))
found.extend(checkVertical(board))
found.extend(checkDiagonal(board))

if "X" in found:
    print("Johan har vunnit")
elif "O" in found:
    print("Abdullah har vunnit")
else:
    print("ingen har vunnit")