x, y = map(int, input().split())

memo = []
data = []

# data = [[int(i) for i in input().split()] for row in range(y)]

for row in range(y):
    memo.append([])
    data.append([])
    nums = [int(i) for i in input().split()]
    for col in range(x):
        memo[row].append(0)
        data[row].append(nums[col])
        if row == 0 or row == y-1:
            memo[row][col] = memo[row][col] + 1
        if col == 0 or col == x-1:
            memo[row][col] = memo[row][col] + 1

        if row > 0:
            if data[row - 1][col] > data[row][col]:
                memo[row][col] = memo[row][col] + 1
                # memo[row-1][col] = memo[row-1][col] + 1
            elif data[row - 1][col] < data[row][col]:
                # pass
                memo[row - 1][col] = min(memo[row - 1][col] + 1,4)
            if data[row - 1][col] == data[row][col]:
                memo[row][col] = memo[row][col] + 1
                memo[row-1][col] = memo[row-1][col] + 1
        if col > 0:
            if data[row][col - 1] > data[row][col]:
                memo[row][col] = memo[row][col] + 1
                # memo[row][col-1] = memo[row][col-1] + 1
            elif data[row][col - 1] < data[row][col]:
                # pass
                memo[row][col - 1] = min(memo[row][col - 1] + 1,4)
            if data[row][col-1] == data[row][col]:
                memo[row][col] = min(memo[row][col] + 1,4)
                memo[row][col-1] = min(memo[row][col-1] + 1,4)
    # print(memo)

changed = True
c = 0
while changed:
    c += 1
    changed = False
    for row in range(y):
        for col in range(x):
            if row > 0:
                if data[row - 1][col] == data[row][col]:
                    if memo[row-1][col] < 4 and memo[row][col] == 4:
                        memo[row][col] = memo[row][col] - 1
                        changed = True
            if row < y-1:
                if data[row + 1][col] == data[row][col]:
                    if memo[row+1][col] < 4 and memo[row][col] == 4:
                        memo[row][col] = memo[row][col] - 1
                        changed = True
            if col > 0:
                if data[row][col-1] == data[row][col]:
                    if memo[row][col-1] < 4 and memo[row][col] == 4:
                        memo[row][col] = memo[row][col] - 1
                        changed = True
            if col < x-1:
                if data[row][col+1] == data[row][col]:
                    if memo[row][col+1] < 4 and memo[row][col] == 4:
                        memo[row][col] = memo[row][col] - 1
                        changed = True
    for row in range(y-1, -1, -1):
        for col in range(x-1, -1, -1):
            if row > 0:
                if data[row - 1][col] == data[row][col]:
                    if memo[row-1][col] < 4 and memo[row][col] == 4:
                        memo[row][col] = memo[row][col] - 1
                        changed = True
            if row < y-1:
                if data[row + 1][col] == data[row][col]:
                    if memo[row+1][col] < 4 and memo[row][col] == 4:
                        memo[row][col] = memo[row][col] - 1
                        changed = True
            if col > 0:
                if data[row][col-1] == data[row][col]:
                    if memo[row][col-1] < 4 and memo[row][col] == 4:
                        memo[row][col] = memo[row][col] - 1
                        changed = True
            if col < x-1:
                if data[row][col+1] == data[row][col]:
                    if memo[row][col+1] < 4 and memo[row][col] == 4:
                        memo[row][col] = memo[row][col] - 1
                        changed = True


count = 0
for row in range(y):
    for col in range(x):
        if memo[row][col] == 4:
            count += 1

# for i in memo:
#     print(i)
# print(c)

print(count)
