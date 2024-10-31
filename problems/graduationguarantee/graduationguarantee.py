n, m = map(int, input().split())

probs = [float(i) for i in input().split()]

probs.sort(reverse=True)
# print(probs)

# problems used, points earned
dp = [0]*(2*n+2)
prevDp = [0]*(2*n+2)

worstCase = n
prevDp[worstCase] = 1
sol = 0
for i in range(1, n+1):
    for j in range(-i, i+1):
        # gets problem right
        dp[j+worstCase+1] += prevDp[j+worstCase] * probs[i-1]
        # gets problem wrong
        dp[j+worstCase-1] += prevDp[j+worstCase] * (1-probs[i-1])
    probSuccess = 0
    for j in range(worstCase+m, worstCase+i+1):
        probSuccess += dp[j]
    sol = max(sol, probSuccess)
    prevDp = dp.copy()
    dp = [0]*(2*n+2)

print(sol)

# for i in dp:
    # print(i)
