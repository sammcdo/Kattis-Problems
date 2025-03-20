board = "".join([input() for _ in range(4)])

letters = "ABCDEFGHIJKLMNO"

def toCoords(index):
    row = index//4
    col = index % 4
    return row, col

off = 0
for i in letters:
    r1,c1 = toCoords(board.index(i))
    r2,c2 = toCoords(letters.index(i))
    off += abs(r1-r2) + abs(c2-c1)

print(off)
