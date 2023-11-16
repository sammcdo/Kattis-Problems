breaks, price = map(int, input().split())

break_list = [int(i) for i in input().split()]

profits = []

for i in range(len(break_list)):
    profits.append(break_list[i] - price)

m = 0
dp = [0] * breaks
dp[0] = profits[0]
for i in range(1, len(profits)):
    dp[i] = profits[i]
    if dp[i-1] > 0:
        dp[i] += dp[i-1]

    if dp[i] > m:
        m = dp[i]

print(m)