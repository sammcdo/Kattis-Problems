n,s,m = map(int, input().split())

board = [int(i) for i in input().split()]

visited = set()
i = s-1
hops = 0
while True:
    # print(i, board[i])
    if i < 0:
        print("left")
        print(hops)
        exit()
    if i >= n:
        print("right")
        print(hops)
        exit()
    if board[i] == m:
        print("magic")
        print(hops)
        exit()
    if i in visited:
        print("cycle")
        print(hops)
        exit()
    visited.add(i)
    if board[i] > 0:
        i += board[i]
        hops += 1
    else:
        i -= abs(board[i])
        hops += 1