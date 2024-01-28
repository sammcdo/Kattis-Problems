t = int(input())
n = int(input())

dishes = [int(input()) for _ in range(n)]

dp = [0] * (t + 1)

dp[0] = 1

for i in range(len(dp)):
    for d in dishes:
        if i - d < 0:
            continue
        else:
            dp[i] += dp[i-d]

print(dp[-1])