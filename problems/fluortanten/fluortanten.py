num = int(input())

line = input().split()

line = [int(i) for i in line]
line.remove(0)

dp = [[0,0,0] for _ in range(len(line)+1)]

a = sum([line[i] * (i+1) for i in range(len(line))])
dp[-1] = [a, 0, a]

for i in range(len(line)-1, -1, -1):

    dp[i][0] = dp[i+1][0] - line[i]*(i+1)

    dp[i][1] = dp[i+1][1] + line[i]*(i+2)

    dp[i][2] = dp[i][0] + dp[i][1]


l = [r[2] for r in dp]

print(max(l))
