main = "abcdefghijklmnopqrstuvwxyz"
alt = input()

# find LCS

dp = [[0]*(len(main)+1) for i in range(len(alt)+1)]

for i in range(len(alt)):
    for j in range(len(main)):
        if alt[i] == main[j]:
            dp[i+1][j+1] = 1 + dp[i][j]
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(26-dp[-1][-1])