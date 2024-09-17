case = 1
while 1:
    w, l = map(int, input().split())
    if w == l == 0:
        break

    board = []
    dir = -1
    x = -1
    y = -1
    for _ in range(l):
        line = list(input())
        if "*" in line:
            if _ == 0:
                dir = 3
                x = line.index("*")
                y = 0
            elif _ == l-1:
                dir = 1
                x = line.index("*")
                y = _
            elif line[0] == "*":
                dir = 0
                x = 0
                y = _
            elif line[-1] == "*":
                dir = 2
                x = w - 1
                y = _
        
        board.append(line)

    moves = [
        [1, 0],
        [0, -1],
        [-1, 0],
        [0, 1]
    ]
    # the light moves
    while 1:
        # print(dir)
        x += moves[dir][0]
        y += moves[dir][1]

        if board[y][x] == "/":
            if dir == 0: dir = 1
            elif dir == 1: dir = 0
            elif dir == 2: dir = 3
            elif dir == 3: dir = 2
        elif board[y][x] == "\\":
            if dir == 0: dir = 3
            elif dir == 1: dir = 2
            elif dir == 2: dir = 1
            elif dir == 3: dir = 0
        elif board[y][x] == "x":
            board[y][x] = "&"
            break
            
    
    print(f'HOUSE {case}')
    for row in board:
        print(*row, sep="")
    case += 1