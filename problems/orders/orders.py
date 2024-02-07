n = int(input())
items = [int(i) for i in input().split()]

m = int(input())
orders = [int(i) for i in input().split()]

def solve(items, target):
    dp = [[0 for i in range(target+1)] for i in range(len(items)+1)]
    used = [[-1 for i in range(target+1)] for i in range(len(items)+1)]

    for i in range(1, len(dp)):
        dp[i][0] = 1

    for i in range(1, len(items)+1):
        for j in range(1, target+1):
            if items[i-1] > j:
                dp[i][j] = dp[i-1][j]
                used[i][j] = used[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-items[i-1]]
                # used[i][j] = used[i - 1][j]
                if dp[i][j-items[i-1]] > 0:
                    used[i][j] = [i, (i,j-items[i-1])]
                elif dp[i-1][j] > 0:
                    used[i][j] = [-1, (i-1, j)]

    return dp, used

dp, used = solve(items, max(orders))

for i in orders:
    if dp[-1][i] == 0:
        print("Impossible")
    elif dp[-1][i] > 1:
        print("Ambiguous")
    else:
        x = []
        next = used[-1][i]
        while next:
            if next == -1:
                break
            a, coord = next
            if a != -1:
                x.append(a)
            next = used[coord[0]][coord[1]]
        print(*list(sorted(x)))