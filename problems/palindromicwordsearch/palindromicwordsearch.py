r,c = map(int, input().split())

grid = [list(input()) for i in range(r)]

rowLookup = [[1]*c for _ in range(r)]
colLookup = [[1]*c for i in range(r)]

# palindromes like aba, xyzyx etc
def findOddPal(rS, cS, isRow):
    if isRow:
        i, j = cS-1, cS+1
        while i >= 0 and j < c and grid[rS][i] == grid[rS][j]:
            i -= 1
            j += 1
        l = j - i - 1
        for x in range(i+1, j):
            rowLookup[rS][x] = max(rowLookup[rS][x], l)
    else:
        i, j = rS-1, rS+1
        while i >= 0 and j < r and grid[i][cS] == grid[j][cS]:
            i -= 1
            j += 1
        l = j - i - 1
        for x in range(i+1, j):
            colLookup[x][cS] = max(colLookup[x][cS],l)

# palindromes like bb, abba, abccba
def findEvenPal(rS,cS, isRow):
    if isRow:
        if cS + 1 < c and grid[rS][cS] == grid[rS][cS+1]:
            i, j = cS-1, cS+2
            while i >= 0 and j < c and grid[rS][i] == grid[rS][j]:
                i -= 1
                j += 1
            l = j - i - 1
            for x in range(i+1, j):
                rowLookup[rS][x] = max(rowLookup[rS][x],l)
    else:
        if rS + 1 < r and grid[rS][cS] == grid[rS+1][cS]:
            i, j = rS-1, rS+2
            while i >= 0 and j < r and grid[i][cS] == grid[j][cS]:
                i -= 1
                j += 1
            l = j - i - 1
            for x in range(i+1, j):
                colLookup[x][cS] = max(colLookup[x][cS],l)

for i in range(r):
    for j in range(c):
        findOddPal(i, j, True)
        findOddPal(i, j, False)
        findEvenPal(i, j, True)
        findEvenPal(i, j, False)

best = 0
for i in range(r):
    for j in range(c):
        best = max(rowLookup[i][j] * colLookup[i][j], best)

print(best)