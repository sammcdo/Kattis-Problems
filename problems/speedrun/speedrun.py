g, n = map(int, input().split())

opts = [[int(i) for i in input().split()] for j in range(n)]

opts.sort()

dp = [0 for i in range(24001)]

for i in range(n):
    start = opts[i][0]
    end = opts[i][1]

    dp[end] = dp[start] + 1

    x = len(dp)
    if i < len(opts) - 1:
        x = opts[i + 1][0] + 1

    for j in range(end + 1, x):
        dp[j] = dp[end]

if g <= dp[-1]:
    print("YES")
else:
    print("NO")