n = int(input())

weights = [int(input()) for i in range(n)]

dp = [[0] * 2000 for _ in range(n+1)]

best = 0
for i in range(1, n+1):
    add = []
    this = weights[i-1]
    dp[i][this] = 1
    # print("this", this)
    for j in range(len(dp[0])):
        if dp[i-1][j]:
            dp[i][j] = 1
            # print(j, end=" ")
            if j + this < 2000:
                dp[i][j+this] = 1
    # print()


for i in range(len(dp[0])):
    if dp[-1][i]:
        if abs(1000-best) > abs(1000-i):
            # print(this, best, i)
            best = i
        if abs(1000-best) == abs(1000-i):
            best = max(best, i)
    # print(best)

print(best)